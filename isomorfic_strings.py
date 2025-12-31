'''
Напиши функцію `isomorphic_strings`, яка приймає рядки `first_string`, `second_string` та визначає, чи вони є ізоморфними.
Рядки ізоморфні, якщо кількість та розташування символів в `first_string` є пропорційними до кількості та розташування в `second_string`.
Усі входження конкретних символів мають бути замінені іншими символами зі збереженням їхнього порядку.
```
isomorphic_strings(first_string="egg", second_string="add") is True
isomorphic_strings(first_string="foo", second_string="bar") is False
isomorphic_strings(first_string="paper", second_string="title") is True
```
'''

def isomorphic_strings(first_string: str, second_string: str) -> bool:
    if len(first_string) != len(second_string):
        return False
    isodict = {}
    for letter in range(len(first_string)):
        if first_string[letter] not in isodict:
            if second_string[letter] in isodict.values():
                return False
            isodict[first_string[letter]] = second_string[letter]
        else:
            if isodict[first_string[letter]] != second_string[letter]:
                return False
    return True

print(isomorphic_strings(first_string="egg", second_string="add")
)
print(isomorphic_strings(first_string="foo", second_string="bar")
)
print(isomorphic_strings(first_string="paper", second_string="title")
)