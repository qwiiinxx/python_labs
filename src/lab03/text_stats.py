import sys
from lib.text import tokenize, count_freq, top_n

def main():
    text = sys.stdin.read()
    tokens = tokenize(text)
    freq = count_freq(tokens)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()