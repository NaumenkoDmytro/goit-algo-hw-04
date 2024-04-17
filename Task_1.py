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

def total_salary(path):
    with open(path, 'r', encoding='utf-8') as fh:
        salary_list = list()
        counter = 0
        for line in fh:
            counter += 1
            salary = line.strip().split(',')
            salary = ' '.join(salary)
            salary_num = int(re.sub('\D','',salary))
            salary_list.append(salary_num)
        total_salary=sum(salary_list)
        print(total_salary)
        print(counter)
        average_salary = total_salary / counter

    return total_salary, average_salary



total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")