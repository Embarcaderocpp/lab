from math import exp


def f(x):
    return exp(3 * x / 2) - 2 * (x + 1)**2


def main():
    print("Решение уравнения: e^(3x/2) - 2(x + 1)^2 = 0")
    print("Метод: половинного деления (бисекция)\n")
    
    eps = 1e-5  
    max_iter = 1000  
    

    a = -2.0
    b = 0.0
    step = 0.1
    
    print("Поиск отрезка с корнем...")
    found = False
    x1 = a
    while x1 < b:
        x2 = x1 + step
        if f(x1) * f(x2) <= 0:
            a = x1
            b = x2
            found = True
            break
        x1 = x2
    
    if not found:
        print("Корень на интервале [-2, 0] не найден.")
        return
    
    print(f"Корень отделён на отрезке [{a:.4f}, {b:.4f}]")
    print(f"f(a) = {f(a):.6f}, f(b) = {f(b):.6f}\n")
    
    
    n = 0  
    while (b - a) >= eps and n < max_iter:
        z = (a + b) / 2.0
        if f(z) * f(a) <= 0:
            b = z
        else:
            a = z
        n += 1
    
    x = (a + b) / 2.0
    
    
    print("Результат уточнения:")
    print(f"Корень x ≈ {x:.8f}")
    print(f"Число итераций: {n}")
    print(f"Длина конечного отрезка: {b - a:.10f}")
    print(f"Значение функции f(x) = {f(x):.10f}")
    
    if abs(f(x)) < 1e-5:
        print("Контроль: значение функции близко к нулю — корень найден верно.")
    else:
        print("Внимание: значение функции велико — возможна ошибка.")



main()