x_1 = int(input("x_1: "))
x_2 = int(input("x_2: "))
x_3 = int(input("x_3: "))
x_4 = int(input("x_4: "))

if x_1 < x_2 and x_1 < x_3 and x_1 < x_4:
    result = f"min x = {x_1}"
else:
    if x_2 < x_3 and x_2 < x_4 and x_2 < x_1:
        result = f"min x = {x_3}"
    else:
        if x_3 < x_1 and x_3 < x_2 and x_3 < x_4:
            result = f"min x = {x_3}"
        else:
            result = f"min x = {x_4}"

print(result)