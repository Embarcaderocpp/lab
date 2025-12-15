import random 

itr = int(input("Количество чисел в наборе: "))
i = 0
ans = False
numbers = []
while i <= itr:
    i +=1
    numbers.append(random.randint(0, 100))

print("Набор", numbers)
number = int(input("n: "))
for el in numbers:
    if el == 0:
        continue
    if number % el == 0:
        for  i in numbers:
            if i * el == number:
                ans = True
if ans == True:
    print("Да")
else:
    print("Нет")           
            

           
