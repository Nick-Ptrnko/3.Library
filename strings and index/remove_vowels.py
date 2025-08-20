'''
створи функцію `remove_vowels()`, яка:
1. Приймає рядок `document`.
2. Повертає новий рядок, з якого вилучені всі
голосні літери.
💡 Голосними літерами є
`a`, `e`, `i`, `o`, `u`, `y`
(великі та малі літери).

'''
def remove_vowels(document):
    vowels = {'a','e','i','o','u','y'}
    result_string = ''
    for i in document:
        if i not  in vowels:
            result_string += i
    return result_string
new_doc = input("Введіть рядок з якого потрібно вилучити голосні літери \n")
print(f"Ваш рядок без голосних літер: \n {remove_vowels(new_doc)}")

