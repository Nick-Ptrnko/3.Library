print(list(range(40)))
lst = []
[lst.append(num) for num in range(100) if "3" in str(num)]
print(lst)