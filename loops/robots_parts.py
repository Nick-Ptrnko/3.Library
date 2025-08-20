'''
Напиши функцію `make_stickers()`, яка:
1. Приймає кількість деталей `details_count` і назву частини робота `robot_part`.
2. Повертає список рядків у форматі `"{robot_part} detail #{n}"`, де
`n` — номер деталі по черзі.
Наприклад:
make_stickers(3, "Body")  # ["Body detail #1", "Body detail #2", "Body detail #3"]
make_stickers(4, "Head")  # ["Head detail #1", "Head detail #2", "Head detail #3", "Head detail #4"]
make_stickers(0, "Foot")  # []
'''
def make_stickers(details_count, robot_part):
    list_of_parts = []
    if details_count > 0:
        for n in range(details_count):
            list_of_parts.append(f"{robot_part} detail #{n+1}")
    return list_of_parts
print(make_stickers(0, "Body"))
