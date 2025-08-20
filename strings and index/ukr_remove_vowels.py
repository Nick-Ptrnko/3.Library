'''
Реалізуй функцію, яка приймає рядок українською мовою
і повертає такий же рядок, але великими літерами і без голосних.
Голосними літерами в українській мові є:
аоуеиіяюєї
'''
def remove_ukr_vowels(phrase) -> str:
    result_phrase = ""
    ukr_vowels = "аоуеийіяюєї" + "аоуеийіяюєї".upper()
    for i in phrase:
        if i not in ukr_vowels:
            result_phrase += i.upper()
    return result_phrase
new_phrase = input("Введіть вашу фразу \n")
print(f"""Початкова фраза:
{new_phrase}
Змінена фраза:
{remove_ukr_vowels(new_phrase)}""")