from math import cos

def f(x):
    y = 0.348 + cos(x/4)
    return y


x_0 = int(input("x_0: "))
h_x = int(input("h_x: "))
x_n = int(input("x_n: "))

count_up = 0
count_down  = 0

y_const = 0.55

for x in range(x_0, x_n, h_x):
    if y_const < f(x):
        count_down += 1
    else:
        count_up += 1

print(f"Выше:{count_up}, ниже: {count_down}")