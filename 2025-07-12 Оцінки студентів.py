
def students_grades(name:str, *grade:int) -> str:
    return f"{name} має середній бал {round(sum(grade)/len(grade))}"
print(students_grades('Назар', 12, 10, 11, 11, 11))
print(students_grades('Віка', 10, 11, 12, 9, 12, 12))