def f(x):
    if -2 <= x <= 2:
        return x**2
    elif 2 <= x <= 5:
        return (x - 4)**2
    elif 5 <= x <= 8:
        return (x-6)**2
    

x_0 = int(input("x_0: "))
h_x = float(input("h_x: "))
x_n = int(input("x_n: "))


while x_0 <= x_n + h_x / 3:
    y = f(x_0)
    x_0 += h_x
    if y is None:
        continue
    else:
        print(y)