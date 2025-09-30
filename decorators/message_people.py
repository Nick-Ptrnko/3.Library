'''
Напиши функцію message_people, яка приймає список імен people, створює і повертає функцію print_message.
Внутрішня функція приймає рядок message і в залежності від того, чому дорівнює message
('hello'/'meeting'/'bye') виводить результати, які показані в прикладі. Вона не повинна нічого повертати.
Приклад:
mes_people = message_people(["Alex", "Robert", "Tom"])
mes_people('hello')
# Hello, Alex, Robert, Tom, nice to see you!
mes_people('meeting')
# Alex, Robert, Tom, we have a meeting in an hour, don't be late!
mes_people('bye')
# Bye Alex, Robert, Tom, see you tomorrow!
'''
def message_people(peoples: list) -> callable:
    people_str = ", ".join(peoples)
    
    def print_message(message: str) -> None:
        if message == "hello":
            print(f"Hello, {people_str}, nice to see you!")
        if message == "meeting":
            print(f"{people_str}, we have a meeting in an hour, don't be late!")
        if message == "bye":
            print(f"Bye {people_str}, see you tomorrow!")
    return print_message
mes_people = message_people(["Alex", "Robert", "Tom"])
mes_people('hello')
mes_people('meeting')
mes_people('bye')
