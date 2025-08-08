'''
реалізуй функцію get_lists_sum, яка приймає два списки чисел однакової довжини
та повертає суму всіх елементів цих списків
'''
def get_lists_sum(list_1, list_2):
    sum_two_list = 0
    for i in range(len(list_1)):
        sum_two_list += int(list_1[i]) + int(list_2[i])
    return sum_two_list
my_string1 = input("Введіть перший список \n")
my_list1 = my_string1.split(", ")
my_string2 = input("Введіть другий список \n")
my_list2 = my_string2.split(", ")
print(f"Сумма чисел списків {my_list1} та {my_list2}: {get_lists_sum(my_list1, my_list2)}")
