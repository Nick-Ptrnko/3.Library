
def fibonacci_generator(number: int):
    current_number = 1
    fibonacci_number = 0
    yield fibonacci_number
    for _ in range(number):
        fibonacci_number += current_number
        current_number = fibonacci_number
        yield fibonacci_number
fib_generator = fibonacci_generator(4)
print(next(fib_generator)) # 0 - Число Фібоначчі з номером 0
print(next(fib_generator)) # 1 - Число Фібоначчі з номером 1
print(next(fib_generator)) # 1 - Число Фібоначчі з номером 2
# обчислюється як сума двох попередніх: 1 + 0 = 1
print(next(fib_generator)) # 2 - Число Фібоначчі з номером 3
# обчислюється як сума двох попередніх: 1 + 1 = 2
