from math import sin, cos

x = 0.5
s = 0

def f_a(n):
    if x <=0.5:
        return 2*n
    elif x>0.5:
        return n/2
        

def f_y(s, n):
    y = (sin(x) + 2)/(3 + cos(x)) * s
    return y


for n in range(0, 21):
    s += f_a(n) * x**n
    print(f_y(s, n))