def repeat(times, func):
    def wrapper(*args, **kwargs):
        for _ in range(times):
            func(*args, **kwargs)
    return wrapper

@repeat(4)
def say(message):
    print(message)

say("Python")
