"""
Дано файл, який містить багаторядковий текст без розділових знаків
(слова відокремлюються пробілами та переносом рядків).
Тобі потрібно знайти слова, що починаються з «w» або «W».
Поверни їх у нижньому регістрі у вигляді відсортованого списку.
Якщо файл не містить потрібних слів, поверни порожній список.
Приклади:
"Width world Wide web"
Result: ["web", "wide", "width", "world"]
"WWW Four-bedroom farmhouse in the countryside Wave All of the four double bedrooms are en suite"
Result: ["wave", "www"]
"""
def read_from_file(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        sorted_list = sorted(file.read().lower().split())
        return [word for word in sorted_list if word.startswith("w")]

print(read_from_file("w_file.txt"))