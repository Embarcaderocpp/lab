from math import sin, cos

x = 0.5
s = 0

def f_a(n):
    result = 0
    if x <=0.5:
        result = 2*n
    elif x>0.5:
        result = n/2
    return result
        

def f_y(s, n):
    y = (sin(x) + 2)/(3 + cos(x)) * s
    return y


for n in range(0, 21):
    s += f_a(n) * x**n
    out = f_y(s, n)
    print(out)