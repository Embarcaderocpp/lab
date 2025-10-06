x = float(input("x: "))
y = float(input("y: "))

result = "no"

if y <= -abs(x) + 2 and -2 <= x <= 2 and y >= 0:
    result = f"dot {x}, {y}"

if 1 <= x**2 + y**2 <= 4 and y <= 0 and not (x**2 + y**2 <= 1):
    result = f"dot {x}, {y}"

print(result)