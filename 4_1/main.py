import math
   
x  =  float(input("x:"))
if x > 1:
    print('x=',x,' "При 1<x функция  не определена.")
else:          
    if x < -2:
        result = 3*x+math.sqrt(abs(x+1))
    else:    
        if -2 <= x - 1.5:
            result = (math.sin(x) + math.cos(x)) / (2*x + 1)
        else:
            result = math.e**(-3*x+2*x-1)
    print('x=', x, f"результат: {result}")
