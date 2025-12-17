def input_text() -> str:
    print("Введите текст (для завершения ввода введите пустую строку):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


def input_word() -> str:
    while True:
        word = input("Введите слово для поиска: ").strip()
        if word:
            return word
        else:
            print("Слово не может быть пустым. Попробуйте снова.")


def count_word_occurrences(text: str, word: str) -> int:
    text_lower = text.lower()
    word_lower = word.lower()
    
    for punct in ".,!?;:'\"()[]{}":
        text_lower = text_lower.replace(punct, " ")
    
    words = text_lower.split()
    return words.count(word_lower)


def output_result(word: str, count: int):
    if count == 0:
        print(f"Слово '{word}' не найдено в тексте.")
    elif count == 1:
        print(f"Слово '{word}' встречается 1 раз.")
    else:
        print(f"Слово '{word}' встречается {count} раз(а).")


def main():
    
    print("=== Поиск слова в тексте ===\n")
    
    text = input_text()
    if not text.strip():
        print("Текст пустой. Программа завершена.")
        return
    
    word = input_word()
    
    occurrences = count_word_occurrences(text, word)
    
    print("\nРезультат:")
    output_result(word, occurrences)

main()