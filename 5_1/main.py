group = int(input("Сколько людей? "))

result = "unlimited"

if group == 2:
    result = f"{group} - 2 человека дуэт"

elif group == 3:
     result = f"{group} - 3 человека трио"

elif group == 4:
     result = f"{group} - 4 человека квартет"

elif group == 5:
      result = f"{group} - 5- 5 человек квинтет"

else:
     result = f"infinity"

print(result)