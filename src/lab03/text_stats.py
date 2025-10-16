import sys, os # НАЖАТЬ control + D 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    # читаем весь ввод (до EOF)
    text = sys.stdin.read()

    # нормализация
    norm_text = normalize(text)

    # токенизация
    tokens = tokenize(norm_text)

    # частоты
    freq = count_freq(tokens)

    # топ-5
    top = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
