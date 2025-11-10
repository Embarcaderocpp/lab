x_1 = int(input("x_1: "))
x_2 = int(input("x_2: "))
x_3 = int(input("x_3: "))
x_4 = int(input("x_4: "))

min_x = x_1  

if x_2 < min_x:
    min_x = x_2
if x_3 < min_x:
    min_x = x_3
if x_4 < min_x:
    min_x = x_4

print(f"Минимальное значение x = {min_x}")
