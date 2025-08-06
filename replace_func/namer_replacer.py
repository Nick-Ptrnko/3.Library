original_phrase = input(
    "Введіть вашу фразу \n"
)
replased_phrase = original_phrase.replace(" ", "_")
print(f"Ваша оригінальна фраза: \n {original_phrase} \n",
      f"Ім'я файла: \n {replased_phrase.lower()}"  
)