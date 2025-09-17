def my_decorator(func):
    def wrapper(): # це обгорнута функція (або обгортка)
        print("Щось відбувається до виклику функції.")
        func() # виклик оригінальної функції
        print("Щось відбувається після виклику функції.")
    return wrapper

@my_decorator
def say_hello():
    print("Привіт!")
say_hello()
