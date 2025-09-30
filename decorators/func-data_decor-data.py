def cache(decor_data):
    def inner(func):
        def wrapper(*func_data):
            result = func(*func_data) + decor_data
            return result
        return wrapper
    return inner

@cache(3)
def long_time_func(a: int, b: int, c: int) -> int:
    return (a + b + c)

a1 = 5
b1 = 5
c1 = 2



print(long_time_func(a1, b1, c1))

