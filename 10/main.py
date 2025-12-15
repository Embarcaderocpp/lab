from math import inf
rows = int(input("Введите количество строк и столбцов: "))

matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

value = -inf
iteraro = 0
max_value = []
for row in matrix:
    for el in row:
        if value < el:
            value = el
    max_value.append(el)
    value = -inf
    iteraro += 1

if len(max_value) > 3:
    start = len(max_value)
    while start != 3:
        min_v = min(max_value)
        max_value.remove(min_v)
        start = len(max_value)
    print(*max_value)
else:
    print(*max_value)
    
    
    
    