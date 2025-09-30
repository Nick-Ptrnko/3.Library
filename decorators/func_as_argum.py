def first(msg):
    print(msg)

first("Hello!")
second = first
second("hi")

def plus(x):
    return x+1
def minus(x):
    return x-1

def operation(funct, x):
    return funct(x)

print(operation(plus, 10))
print(operation(minus, 20))

def multiplier(parameter1: int):
    def func_inside(parameter2:int):
        return parameter2*parameter1
    return func_inside
multiply3 = multiplier(3)
print(multiply3(7))
print(multiply3(5))

