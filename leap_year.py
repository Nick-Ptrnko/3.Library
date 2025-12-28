def is_leap_year(year: int) -> bool:
    # write your code here
    modulus_4 = year % 4
    print(year / 4, modulus_4)
    if modulus_4 == 0:
        modulus_100 = year % 100
        print(year / 100, modulus_100)
        modulus_400 = year % 400
        print(year / 400, modulus_400)
        if modulus_400 == 0 or modulus_100 != 0:
            return True
    return False


print(is_leap_year(1984))
