def decorate(func: callable):
    def inner():
        print("Decorate before")
        func()
        print("Decorate after")
    return inner

def printer():
    print("Hello")

decorated_printer = decorate(printer)
decorated_printer()
