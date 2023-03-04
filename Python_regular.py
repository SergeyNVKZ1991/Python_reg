from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
# data_file = []
with open("Data_file.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    date_phone = ''
    for a in f:
        date_phone += a

pattern = r"(\+7|7|8)?[ |s]?([\(]?(\d{3})[\)]?)[ |s|-]*(\d+)[ |s|-]*(\d{2})[s|-]*(\d{2})"
result = re.sub(pattern, r"+7 (\3)\4-\5-\6", date_phone)


text = result.split('\n')
# pprint(text)
splitted = [[]]
for i in text[1:]:
    splitted.append([i])

# dict_persone = {}
# for string in splitted:
#     for i in string:
#         if string[0] not in dict_persone:
#             dict_persone[string[0]] = string[1:]
# #
# pprint(dict_persone)


## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w", encoding='utf-8') as f:
#        datawriter = csv.writer(f, delimiter=',')
#
#        # Вместо contacts_list подставьте свой список:
#        datawriter.writerows(dict_persone)
