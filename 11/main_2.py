k = tuple(map(int, input("Введите число").split()) )
number = int(input("Введите число в картеже: "))
try:
    index = k.index(number)
    result = []
    result.append(number)

    for i in range(index+1, len(k)):
        if k[i] == number:
            result.append(2)
            break   
        result.append(k[i])
    
    
    print(f"Кортеж {k}, элемент {number} => {tuple(result)}")
except ValueError as e:
    print(f"Кортеж {k}, элемент {number} => ())")

