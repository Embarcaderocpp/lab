from math import sin, cos, pi


def f(x):
    return (sin(x) + cos(2 * x)) / (2 + cos(x))


def integral_38(a, b, n):
    """
    Вычисляет определённый интеграл от a до b с n разбиениями.
    n должно быть кратно 3.
    """
    if n % 3 != 0:
        print("Ошибка: n должно быть кратно 3!")
        return None
    
    h = (b - a) / n               
    summa = f(a) + f(b)            
    
    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            summa += 2 * f(x)      
        else:
            summa += 3 * f(x)      
    
    integral = 3 * h / 8 * summa   
    return integral


def main():
    print("Численное интегрирование функции (sin x + cos 2x) / (2 + cos x)")
    print("Правило трёх восьмых (Simpson's 3/8 rule)\n")
    
    a = pi / 3     
    b = pi / 2      
    n = 60          
    
    print(f"Отрезок интегрирования: [{a:.6f}, {b:.6f}] (π/3 до π/2)")
    print(f"n = {n}\n")
    
    I_n = integral_38(a, b, n)
    print(f"Интеграл при n = {n}:    {I_n:.10f}")
    
    I_2n = integral_38(a, b, 2 * n)
    print(f"Интеграл при n = {2*n}:  {I_2n:.10f}")
    
    diff = abs(I_2n - I_n)
    print(f"\nРазница между результатами: {diff:.10f}")
    
    if diff < 1e-10:
        print("Результаты практически совпадают — высокая точность уже при n=60.")


main()