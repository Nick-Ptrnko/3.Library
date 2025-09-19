from typing import Callable
import time

def timer(param1: Callable):
    def inner(*a, **kwa):
        start_time = time.time()
        result = param1(*a, **kwa)
        end_time = time.time()
        return f"Time of range {end_time - start_time}\nSum: {result}"
    return inner

def decorate(func: Callable): #Функція-декоратор
    def inner(*a, **kwa):
        print("Decorate before")
        print(func(*a, **kwa))
        print("Decorate after")
    return inner

@timer
@decorate
def long_func() -> int:
    return sum(range(int(1.0e7)))

print(long_func())


'''
@timer
def very_long_func(numbr: int) -> int:
    return sum(range(numbr))
print(f"Keywords arg\n{very_long_func(numbr=10_000_000)}")
print(f"Args\n{very_long_func(10_000_000)}")'''

