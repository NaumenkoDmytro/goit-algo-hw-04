'''
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.
Наприклад:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

'''

import re
from open_file import read_file

def get_cats_info(path):
    final_list = []
    lines = read_file(path)
    for line in lines:
        try:
            split_the_line = line.strip().split(',')
            if len(split_the_line) == 3: #without this check I had AttributeError: 'list' object attribute 'append' is read-only how to fix it
                    cat_info = {
                        'id': split_the_line[0],
                        'name': split_the_line[1], 
                        'age': split_the_line[2]
                    }
                    final_list.append(cat_info)
        except Exception as e:
                print(f"Error: {e}")
    return final_list


cats_info = get_cats_info("cats_file.txt")
print(cats_info)

#discuss with mentor

# def get_cats_info(path):
#     with open(path, 'r', encoding='utf-8') as fh:
#         final_list = list()
#         for line in fh:
#             split_the_line = line.strip().split(',')
#             print(type(split_the_line))
#             for item in split_the_line:
#                 final_list.append =({
#                     'id' : item[0],
#                     'name': item[1],
#                     'age": item[2]
#                 })
# here is my code but it has AttributeError: 'list' object attribute 'append' is read-only how to fix it