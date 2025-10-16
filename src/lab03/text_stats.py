import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    # Читаем весь ввод (до EOF)
    text = sys.stdin.read()

    # Нормализация
    norm_text = normalize(text)

    # Токенизация
    tokens = tokenize(norm_text)

    # Частоты
    freq = count_freq(tokens)

    # Топ-5
    top = top_n(freq, n=5)

    # Вывод
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()


# Всего слов: <N>
# Уникальных слов: <K>
# Топ-5: — по строке на запись в формате слово:кол-во (по убыванию, как в top_n).
