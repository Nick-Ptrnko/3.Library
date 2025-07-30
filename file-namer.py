original_phrase = input(
    "Программа для перетворення рядка на ім'я файлу \n"
    "Введіть фразу \n"
)
lower_frase = original_phrase.lower()
result_frase = ""
for i in lower_frase:
    if i == " ":
        result_frase += "_"
    else:
        result_frase += i
print(f"Оригінальна фраза:\n {original_phrase} \n Назва файла: \n {result_frase}")
