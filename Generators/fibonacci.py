def fibonacci_generator(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib_generator = fibonacci_generator(6)
for fib_number in fib_generator:
    print(fib_number)
# 0
# 1
# 1 (1 + 0)
# 2 (1 + 1)
# 3 (2 + 1)
# 5 (3 + 2)
