'''
написати функцію make_hello_function(), яка просто повертає іншу функцію.
Ця внутрішня функція при виклику має друкувати "Привіт!".

def make_hello_function():
    def hello():
        print("Hello, world!")
    return hello

hello1 = make_hello_function()
hello1()

def proxy_print(*args):
    print(*args)
proxy_print("Python", "це", "круто")
proxy_print(1, 2)
'''
from typing import Callable


def composition(first_function: Callable, second_function: Callable) -> Callable:
    def wrapper(*args) -> Callable:
        result = first_function(second_function(*args))
        return result
    return wrapper

first_function = lambda a: 2 * a + 3
second_function = lambda a: a ** 2
print(composition(first_function, second_function)(2))

first_function = lambda a: 2 * a + 3
second_function = lambda a, b: a + b
print(composition(first_function, second_function)(2, 3))