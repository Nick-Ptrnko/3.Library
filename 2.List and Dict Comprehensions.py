'''
print(list(range(40)))
lst = []
[lst.append(num) for num in range(100) if "3" in str(num)]
print(lst)
'''

'''
Напиши функцію `all_targets_hit_upgrade`, яка приймає результати пострілів у кожну мішень.
Результати - це список, кожен елемент якого являється списком булевих значень, які відповідають результатам пострілів
у одну з мішеней. Якщо значення `True`, то значить даним пострілом мішень була вражена, якщо `False`, то
значить ні. Таким чином, якщо у списку хоча б одне значення `True`, то мішень була вражена, якщо всі `False`, то ні.

Функція `all_targets_hit_upgrade` повертає `True`, якщо усі мішені були вражені.
Функція повинна містити тільки конструкцію `return`. Використовуй list comprehension.
Також для розв'язання цієї задачі дуже зручно використовувати функції `any` та `all`
Наприклад:
attempts1 = [
  [True, False, True],  # Постріли у першу мішень
  [False, True, False, True],  # Постріли у другу мішень
  [False, True],  # Постріли у третю мішень
 ]
all_targets_hit_upgrade(attempts) is True # всі мішені були вражені хоча б один раз
attempts2 = [
  [True, False, True],  # Постріли у першу мішень
  [False, False, True],  # Постріли у другу мішень
  [False, False],  # Постріли у третю мішень
 ]
all_targets_hit_upgrade(attempts) is False # Третя мішень не була вражена




                    МОЄ ВИРІШЕННЯ ЗАДАЧІ ЧЕРЕЗ "ОДИН РЯДОК"
'''
attempts1 = [
  [True, False, True],  # Постріли у першу мішень
  [False, True, False, True],  # Постріли у другу мішень
  [False, True],  # Постріли у третю мішень
 ]
attempts2 = [
  [True, False, True],  # Постріли у першу мішень
  [False, False, True],  # Постріли у другу мішень
  [False, False],  # Постріли у третю мішень
 ]
'''
def all_targets_hit_upgrade(attempts: list) -> bool:
    return all([any(targets) for targets in attempts])

print(all_targets_hit_upgrade(attempts1))
'''

'''
                        ПОКРАЩЕННЯ КОДУ ВІД ШІ
Minor Refinement (Optional - for extreme memory optimization):
As mentioned, if attempts could potentially contain millions of targets, and memory is a critical concern, you could
switch the list comprehension [] to a generator expression ():
This change primarily affects memory usage, not the overall logic or correctness. For most typical use cases,
your current version is already excellent.

'''
def all_targets_hit_upgrade(attempts: list[list[bool]]) -> bool:
    # Adding more precise type hint for clarity
    return all(any(targets) for targets in attempts) # Note the parentheses instead of square brackets

print(all_targets_hit_upgrade(attempts1))


#                   ВИРІШЕННЯ ЗАДАЧІ ЧЕРЕЗ ЦИКЛ (МОЄ)
'''
def all_targets_hit(attempts_for_each_target: list) -> bool:
    for target in attempts_for_each_target:
       if any(target) is False:
           res = False
           break
       else: res = True
    return res
print(all_targets_hit([[True, False, True], [False, True, False, False], [False, True]]))


#                   РІШЕННЯ МЕНТОРА
'''

attempts3 = []
'''
def all_targets_hit(attempts_for_each_target: list) -> bool:
    targets_results = []
    for current_target_attempts in attempts_for_each_target:
        targets_results.append(any(current_target_attempts))
    return all(targets_results)

print(all_targets_hit(attempts3))

#                   ВРАЖАЮЧЕ СВОЄЮ ГЕНІАЛЬНІСТЮ РІШЕННЯ ВІД ШІ
'''
'''
def all_targets_hit(attempts_for_each_target: list[list[bool]]) -> bool:
    """
    Перевіряє, чи були всі мішені вражені хоча б один раз.

    Аргументи:
        attempts_for_each_target (list[list[bool]]): Список, де кожен внутрішній список
                                                    представляє результати пострілів по одній мішені.
                                                    True означає влучання, False - промах.

    Повертає:
        bool: True, якщо всі мішені були вражені хоча б один раз;
              False, якщо якась із мішеней не була вражена.
    """
    # 1. Обробка порожнього вхідного списку
    if not attempts_for_each_target:
        return True # Якщо мішеней немає, вважаємо, що всі "вражені"

    for target in attempts_for_each_target:
        # 2. Більш ідіоматична перевірка та ранній вихід
        if not any(target): # Якщо для поточної мішені немає жодного True (тобто всі False)
            return False    # Ця мішень не вражена, тому одразу повертаємо False

    # 3. Якщо цикл завершився, значить, всі мішені були вражені
    return True

print(all_targets_hit(attempts1))
'''