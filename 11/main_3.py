k = tuple(map(int, input("Введите число").split()) )
number = int(input("Введите число в картеже: "))
index = k.index(number)
result = []
for i in range(0, len(k)):
    if i == index:
        continue
    result.append(k[i])
result = tuple(result)
print(f"Кортеж {k}, удаляемый эл-т {number} => {result}")