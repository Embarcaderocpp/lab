group = int(input("Сколько людей? "))

def groups(group):  
    result = "unlimited"

    match group:
        case 2:
            result = f"{group} - 2 человека дуэт"

        case 3:
            result = f"{group} - 3 человека трио" 

        case 4:
            result = f"{group} - 4 человека квартет"

        case 5:
            result = f"{group} - 5- 5 человек квинтет"

    return result

print(groups(group))