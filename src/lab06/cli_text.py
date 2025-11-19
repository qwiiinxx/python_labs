import argparse
from src.lib.text import normalize, tokenize, count_freq, top_n

# запуск через  'python3 -m src.lab06.cli_text stats --input data/samples/test_stats.txt --top 5'
def main():

    parser = argparse.ArgumentParser(description="Пример CLI")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Входной файл")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-n")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    args = parser.parse_args()

    if args.command == "stats":
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            parser.error(f"Файл не найден")
        if not text:
            parser.error("Входной файл пуст")

        norm_text = normalize(text)
        tokens = tokenize(norm_text)
        freq = count_freq(tokens)
        top = top_n(freq, n=args.top)

        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print("Топ-{}:".format(args.top))
        for word, count in top:
            print(f"{word}:{count}")

    elif args.command == "cat":
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, start=1):
                    if args.n:
                        print(f"{i}\t{line}", end="")
                    else:
                        print(line, end="")
        except FileNotFoundError:
            parser.error(f"Файл не найден")
    elif args.command is None:
        parser.error("Не указана подкоманда")
        
if __name__ == "__main__":
    main()
