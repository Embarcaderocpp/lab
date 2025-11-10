import math

def f(x):
    if x < -2:
        result = 3*x+math.sqrt(abs(x+1))
    if -2 <= x - 1.5:
        result = (math.sin(x) + math.cos(x)) / (2*x + 1)
    if -1 < x <= 1:
        result = math.e**(-3*x+2*x-1)
    if x > 1:
        result = "При 1<x функция  не определена."
    return result
    
x  =  float(input("x:"))
result = f(x)
print(f"результат: {result}")