'''
Напиши генератор time_range, який приймає два аргументи, час початку та час закінчення: time_start, time_end
- кортежі з трьома цілими hours, minutes, seconds.
На першій ітерації time_range повинен повертати початковий час time_start, на кожній наступній ітерації він повертає
попереднє значення, збільшене на одну секунду.
Приклад:
t_range = time_range(time_start=(10, 0, 0),
                     time_end=(10, 0, 3))
next(t_range) == (10, 0, 0)
next(t_range) == (10, 0, 1)
next(t_range) == (10, 0, 2)
next(t_range)
# Error: StopIteration

Час закінчення може бути меншим за початковий.
t_range = time_range(time_start=(23, 59, 59),
                     time_end=(0, 0, 3))
t_range_list = list(t_range)
t_range_list == [
  (23, 59, 59),
  (0, 0, 0),
  (0, 0, 1),
  (0, 0, 2)
]
'''

def time_range(time_start: tuple, time_end: tuple) -> tuple:
    hours, minutes, seconds = time_start
    current_time = hours, minutes, seconds
    while current_time != time_end:
        yield current_time
        seconds += 1
        if hours == 23 and minutes == 59 and seconds == 60:
            hours = 0
            minutes = 0
            seconds = 0
        elif minutes == 59 and seconds == 60:
            hours += 1
            minutes = 0
            seconds = 0
        elif seconds == 60:
            minutes += 1
            seconds = 0
        current_time = hours, minutes, seconds

t_range = time_range(time_start=(23, 59, 57),
                     time_end=(0, 0, 3))
print(next(t_range))
print(next(t_range))
print(next(t_range))
print(next(t_range))
print(next(t_range))
print(next(t_range))
print(next(t_range))
