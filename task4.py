'''
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.

У цій домашній роботі зосередимося на інтерфейсі самого бота. Найпростіший і найзручніший на початковому етапі розробки інтерфейс - це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати. 
Будь-який CLI складається з трьох основних елементів:
1)Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
2)Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
3)Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.

На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. 
Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.
'''
#Function that show all contacts.
def show_all(contacts):
    return contacts
#Function that show Phone number by users name.
def show_phone(args, contacts):
    if args:
        name = args[0]
        if name in contacts: #Check if we have this contact in the dictionary
            return contacts[name]
        else:
            return f'User name is empty' 
    else:
        return f'User name was not provided' 

#Function that change a phone number by users name.   
def change_contact(args, contacts):
    if len(args) < 2: #check if we have all arguments to work with from the list
        return f'Enter exactly two pieces of data: name and phone'
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f'The contact  for {name}, was updated :)'


def parse_input(user_input):
    user_input = user_input.strip() 
    if not user_input: #check if user just pressed the "Enter" button
        return []
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2: #check if we have all arguments to work with from the list
        return f'Enter exactly two pieces of data: name and phone'
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()