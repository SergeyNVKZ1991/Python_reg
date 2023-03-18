# from pprint import pprint
# import csv
# import re
#
# # читаем адресную книгу в формате CSV в список contacts_list
# with open("Data_file.csv") as f:
#     rows = csv.reader(f, delimiter=",")
#     contacts_list = list(rows)
#
# # Создаем новый список контактов, где ФИО помещены в отдельные столбцы lastname, firstname, surname
#
# new_list = []
# for contact in contacts_list:
#     contact[:3] = [' '.join(contact[:3])]
#     new_list.append(contact)
#
# new_contact_list = []
# for el in new_list:
#     for record in el:
#         record = el[0].split()
#         record.extend(el[1:])
#     new_contact_list.append(record)
#
# # Приводим все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
#
# pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)' \
#           '(\s*)(\-*)(\d{3})(\-)*(\d{2})(\-)*(\d{2})*' \
#           '(\s)*(\()*(доб\.)*(\s)*(\d+)*(\))*'
#
# repl = r'+7(\4)\8-\10-\12 \15\17'
#
# new_list = []
# for new_contact in new_contact_list:
#     contacts_string = ','.join(new_contact)
#     new_contacts_string = re.sub(pattern, repl, contacts_string)
#     format_contacts = new_contacts_string.split(',')
#     new_list.append(format_contacts)
# pprint(new_list)
#
# # Объединяем все дублирующиеся записи о человеке в одну.
# new_list_2 = []
# new_dict = {}
# res = {}
#
# for i in new_list:
#     # if record in new_list_2:
#     for record in new_list_2:
#         if i[0] in record.keys():
#
#             for v in record.values():
#                 if v[0] == '':
#                     v[0] = i[1]
#                 elif v[1] == '':
#                     v[1] = i[2]
#                 elif v[2] == '':
#                     v[2] = i[3]
#                 elif v[3] == '':
#                     v[3] = i[4]
#                 elif v[4] == '':
#                     v[4] = i[5]
#                 elif v[5] == '':
#                     v[5] = i[6]
#                 record.update({i[0]: v})
#
#     else:
#         record = {i[0]: i[1:]}
#         new_list_2.append(record)
# # pprint(new_list_2)
# #
# ## 2. Сохраните получившиеся данные в другой файл.
# ## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#
#     ## Вместо contacts_list подставьте свой список:
#     datawriter.writerows(new_list)
#
# with open('phonebook.csv') as f:
#     print(f.read())

import re
import csv
from pprint import pprint
from collections import defaultdict

# Читаем адресную книгу в формате CSV в список contacts_list:
with open("Data_file.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    # Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
    phone_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                    r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                    r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    phone_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'

    contacts_list_new = []
    for page in contacts_list:
        page_string = ','.join(page)
        format_page = re.sub(phone_pattern, phone_pattern_new, page_string)
        page_list = format_page.split(',')
        contacts_list_new.append(page_list)

    # Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
    name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                   r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'

    contacts_list = []
    for page in contacts_list_new:
        page_string = ','.join(page)
        format_page = re.sub(name_pattern, name_pattern_new, page_string)
        page_list = format_page.split(',')
        if page_list not in contacts_list:
            contacts_list.append(page_list)


# Объединить все дублирующиеся записи о человеке в одну.
new_list = defaultdict(list)
for info in contacts_list:
    key = tuple(info[:2])
    for item in info:
        if item not in new_list[key]:
            new_list[key].append(item)

result_list = list(new_list.values())

# Записать занные в новую адресную книгу
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)
    print('Данные успешно записаны записаны ..')

# with open('phonebook.csv', unicode='utf=8') as f:
#     print(f.read())