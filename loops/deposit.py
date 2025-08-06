start_sum = float(input("Введіть початкову суму \n"))
increment = float(input("Введіть скільки будете відкладати в місяць \n"))
sum = start_sum
for i in range(12):
    print(f"В {i+1} місяць маємо {sum/1000000} млн.")
    sum += increment


