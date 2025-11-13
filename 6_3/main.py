    

x_0 = int(input("x_0: "))
h_x = int(input("h_x: "))
x_n = int(input("x_n: "))
x = x_0
while x <= x_n + h_x/3:
    if x < -2 or x > 8:
        print(f'{x = :.10.2f}\tФУНКЦИЯ НЕ ОПР')
    else:
        if -2 <= x <= 2:
            y = x**2
        elif 2 <= x <= 5:
            y = (x - 4)**2
        else:
            y = (x-6)**21
        print(f'{x = :.10.2f}\t{y = :.10.2f})
    x += h_x
