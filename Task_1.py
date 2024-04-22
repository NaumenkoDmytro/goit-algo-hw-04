'''
У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. 
Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

Наприклад:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
'''
import re
from File_Utility import read_file


def total_salary(path):
    lines = read_file(path) #I wrote my own file open module to handle errors
    counter = 0
    total_salary = 0
    try:
        for line in lines:
            counter += 1
            _, salary = line.strip().split(',')
            total_salary += int(salary)
        average_salary = total_salary / counter
        return total_salary, average_salary
    except ZeroDivisionError: #in this case we could have / 0 error becaue if the file path was broken the function return 0 and go ahead with calculations
        print("I think something wrong with the file path") 
        return None


    



total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



# def total_salary(path):
#     lines = read_file(path)
#     salary_list = list()
#     counter = 0
#     try:
#     for line in lines:
#         counter += 1
#         salary = line.strip().split(',')
#         salary = ' '.join(salary)
#         salary_num = int(re.sub('\D','',salary))
#         salary_list.append(salary_num)
#     total_salary=sum(salary_list)
#     average_salary = total_salary / counter

#     return total_salary, average_salary



# total, average = total_salary('salary_fe.txt')
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")