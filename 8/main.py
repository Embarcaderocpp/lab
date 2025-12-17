
x_0 = int(input("x_0: "))
h_x = int(input("h_x: "))
x_n = int(input("x_n: "))


n_start_pi = 1
n_end_pi = 8
n_start_sigma = 0
n_end_sigma = 7  


if h_x <= 0:
    print("Ошибка: h_x должен быть > 0")
elif x_n < x_0:
    print("Ошибка: x_n должен быть >= x_0")
else:
    
    print("x\t Y(x)")
    print("-" * 10)
    
    x = x_0
    for i in range(x_0, x_n, h_x):
        if x > 0:
            prod = 1.0
            for n in range(n_start_pi, n_end_pi + 1):
                member = 1 + (x ** n) / n  
                prod *= member  
            y = x / (x+1) * prod
        else:
            summ = 0.0
            for n in range(n_start_sigma, n_end_sigma + 1):  
                term = (x ** n) / (n + 1)  
                summ += term 
            y = summ
        
        
        print(f"{x:.2f}\t {y:.4f}")
        x += h_x