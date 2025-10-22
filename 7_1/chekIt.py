xs = []
ys = []

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
 
x = x_0

while x_0 <= x_n:
    x_0 += h_x
    y = f(x_0)
    if y is None:
        continue
    else:
        ys.append(y)
        xs.append(x_0)
        #print(y)

import matplotlib.pyplot as plt

# ... в цикле: xs.append(x); ys.append(y)
plt.plot(xs, ys, 'o-')  # Точки и линия
plt.show()