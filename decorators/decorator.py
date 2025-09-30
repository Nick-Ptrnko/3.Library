def decorate(func): #Функція-декоратор
    def inner():
        print("Decorate before")
        func()
        print("Decorate after")
    return inner

'''def printer(): #Функція, яку декоруємо
    print("Hello")

decorated_printer = decorate(printer) #Присвоєння змінній decorated_printer результату виконання функції inner зі змінною printer
decorated_printer() #Нова функція (по суті задекорована функція printer())'''

#Рядок 11 можна замінити рядком 15:
@decorate
def printer(): #Функція, яку декоруємо
    print("Hello")

printer() #Тепер викликаючи функцію за її попереднім ім'ям, отримуємо нову - задекоровану функцію

