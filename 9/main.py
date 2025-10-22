arr = sorted([int(input("Введите элемент: ")) for i in range(int(input("введите количество элементов: ")))])
if len(arr)> 0:
     arr[0], arr[-1] = arr[-1], arr[0]

print(arr)


            
