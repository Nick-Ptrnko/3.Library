'''
Напиши функцію `double_power()`, яка приймає список потужностей `current_powers` та повертає список із
подвоєними значеннями.
💡 Якщо список порожній, функція має повернути порожній список
'''
def double_power(current_powers):
	double_powers = []
	for power in current_powers:
		double_powers.append(float(power)*2)
	return double_powers
user_powers = input("Введіть список потужностей \n")
if user_powers == "":
	print([])
else:
	print(f"Подвоєна потужність:\n  {double_power(user_powers.split(", "))}")
