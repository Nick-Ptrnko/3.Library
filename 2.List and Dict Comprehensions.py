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
'''
def all_targets_hit_upgrade(attempts: list) -> bool:
    return all([any(targets) for targets in attempts])

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
print(all_targets_hit_upgrade(attempts1))


