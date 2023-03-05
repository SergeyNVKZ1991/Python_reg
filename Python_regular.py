from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("Data_file.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Создаем новый список контактов, где ФИО помещены в отдельные столбцы lastname, firstname, surname

new_list = []
for contact in contacts_list:
    contact[:3] = [' '.join(contact[:3])]
    new_list.append(contact)

new_contact_list = []
for el in new_list:
    for record in el:
        record = el[0].split()
        record.extend(el[1:])
    new_contact_list.append(record)

# Приводим все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;

pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)' \
          '(\s*)(\-*)(\d{3})(\-)*(\d{2})(\-)*(\d{2})*' \
          '(\s)*(\()*(доб\.)*(\s)*(\d+)*(\))*'

repl = r'+7(\4)\8-\10-\12 \15\17'

new_list = []
for new_contact in new_contact_list:
    contacts_string = ','.join(new_contact)
    new_contacts_string = re.sub(pattern, repl, contacts_string)
    format_contacts = new_contacts_string.split(',')
    new_list.append(format_contacts)
# pprint(new_list)

# # Объединяем все дублирующиеся записи о человеке в одну.
new_list_2 = []
new_dict = {}
res = {}

for i in new_list:
    # if record in new_list_2:
    for record in new_list_2:
        if i[0] in record.keys():

            for v in record.values():
                if v[0] == '':
                    v[0] = i[1]
                elif v[1] == '':
                    v[1] = i[2]
                elif v[2] == '':
                    v[2] = i[3]
                elif v[3] == '':
                    v[3] = i[4]
                elif v[4] == '':
                    v[4] = i[5]
                elif v[5] == '':
                    v[5] = i[6]
                record.update({i[0]: v})

    else:
        record = {i[0]: i[1:]}
        new_list_2.append(record)
pprint(new_list_2)
