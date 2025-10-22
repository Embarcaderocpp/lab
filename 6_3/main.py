def f(x):
    if -2 <= x <= 2:
        return x**2
    elif 2 <= x <= 5:
        return (x - 4)**2
    elif 5 <= x <= 8:
        return (x-6)**21
    

x_0 = int(input("x_0: "))
h_x = int(input("h_x: "))
x_n = int(input("x_n: "))

for x in range(x_0, x_n, h_x):
    y = f(x)
    print(y)