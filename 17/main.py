import math


x = float(input("Введите x: "))
a = float(input("Введите a (a > 0): "))
eps = float(input("Введите epsilon (погрешность > 0): "))
    
if a <= 0 or eps <= 0:
    print("Ошибка: a должно быть положительным, epsilon > 0.")
    
    
ln_a = math.log(a)
sum_s = 0.0
term = 1.0  
k = 0
iterations = 0
    
while True:
    sum_s += term
    iterations += 1
    k += 1
    term = term * (x * ln_a) / k
    if abs(term) < eps:
        break
    
print(f"Сумма ряда: {sum_s}")
print(f"Число итераций: {iterations}")
