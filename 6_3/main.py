def f(x):
    result = 0
    if -2 <= x <= 2:
        result = x**2
    elif 2 <= x <= 5:
        result = (x - 4)**2
    elif 5 <= x <= 8:
        result = (x-6)**21
    return result
    

x_0 = int(input("x_0: "))
h_x = int(input("h_x: "))
x_n = int(input("x_n: "))

while x_0 <= x_n + h_x/3:
    y = f(x_0)
    print(y)
    x_0 += h_x