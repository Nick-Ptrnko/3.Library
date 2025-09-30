import time

def delay(seconds):
    def inner(func):
        def wrapper(*a, **kwa):
            print(f"Sleep {seconds} seconds")
            for i in range(seconds):
                time.sleep(1)
                print(i+1)
            return func(*a, **kwa)
        return wrapper
    return inner

@delay(seconds = 5)
def printer(name: str) -> None:
    print(f"Hello, {name}")

printer("Mykola")

#printer = delay(5)(printer)
#printer = inner(printer) - попередній рядок delay(5) - це inner з замкнутою змінною 5
#printer("Mykola")

#delay(4)(printer)("Ksyusha")
#inner(printer)("Ksyusha") - попередній рядок delay(4) - це inner з замкнутою змінною 4
#wrapper("Ksyusha") - попередній рядок inner(printer) - це wrapper з замкнутою змінною printer

