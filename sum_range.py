def sum_of_numbers(first_number: int, second_number: int) -> int:
    if first_number < second_number:
        return sum(range(first_number, second_number+1))
    elif first_number == second_number:
        return first_number
    else:
        return sum(range(second_number, first_number+1))

print(sum_of_numbers(1, 2))
print(sum_of_numbers(1, -3))
