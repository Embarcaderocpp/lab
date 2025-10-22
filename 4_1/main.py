import math

def f(x):
    if x < -2:
        return 3*x+math.sqrt(abs(x+1))
    if -2 <= x - 1.5:
        return (math.sin(x) + math.cos(x)) / (2*x + 1)
    if -1 < x <= 1:
        return math.e**(-3*x+2*x-1)
    if x > 1:
        return "При 1<x функция  не определена."
    
x  =  float(input("x:"))
print(f"результат: {f(x)}")