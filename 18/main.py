import math

n = int(input("Введите количество компонент: "))

with open("components.txt", "w") as file:
    for i in range(1, n + 1):
        a_i = (i + 1)**2 * math.sin(i * math.pi / 10)
        file.write(f"{a_i}\n")

components = []
with open("components.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        try:
            value = float(line.strip())
            components.append(value)
        except ValueError:
            print("Ошибка чтения значения из файла.")
            break


print("\nПрочитанные компоненты из файла:")
for idx, val in enumerate(components, start=1):
    print(f"a_{idx} = {val:.6f}")