from datetime import date
def unlucky_days(year: int) -> int:
    cntr = 0
    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            cntr += 1
    return cntr


print(unlucky_days(2015))
print(unlucky_days(1986))