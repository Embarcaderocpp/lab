
def find_min_key(d: dict) -> str:
    min_key = min(d, key=lambda k: d[k])
    return min_key


def main():
    data = {'A': 10, 'B': 3, 'C': 7, 'D': -5, 'E': -30}
    
    print("Словарь:", data)
    
    key = find_min_key(data)
    
    print(f"Ключ с минимальным значением: '{key}'")
    print(f"Минимальное значение: {data[key]}")

main()