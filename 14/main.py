
while True:
    try:
        n = int(input("Введите максимальную цифру (от 2 до 9): "))
        if 2 <= n <= 9:
            break
        else:
            print("Пожалуйста, введите число от 2 до 9.")
    except ValueError:
        print("Введите целое число.")


for i in range(1, n + 1):
   
    spaces = " " * (n - i)
    
    
    if i == 1:
        print(spaces + "1")
    elif i == 2:
        print(spaces + "2*2")
    else:
        stars = "*" * (2 * i - 3)
        print(spaces + f"{i}{stars}{i}")


for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    
    if i == 1:
        print(spaces + "1")
    elif i == 2:
        print(spaces + "2*2")
    else:
        stars = "*" * (2 * i - 3)
        print(spaces + f"{i}{stars}{i}")