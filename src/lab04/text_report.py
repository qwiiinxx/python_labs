from pathlib import Path
import sys, os
import csv
import argparse

# импорт функций из lib/text.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.lib.text import normalize, tokenize, count_freq, top_n


def read_text(path: Path, encoding: str = "utf-8") -> str:
    """Считывает содержимое файла в одну строку."""
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    return path.read_text(encoding=encoding)


def write_csv(rows, path: Path, header=("word", "count")) -> None:
    """Записывает данные в CSV с заголовком."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)


def make_report(in_path: Path, out_path: Path, encoding: str = "utf-8") -> None:
    """Основная логика: чтение, обработка, сохранение."""
    # чтение текста
    text = read_text(in_path, encoding)

    # нормализация, токенизация, подсчёт частот
    norm_text = normalize(text)
    tokens = tokenize(norm_text)
    freq = count_freq(tokens)

    # сортировка по условию: count ↓, word ↑
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # запись в CSV
    if tokens:  # если текст не пуст
        write_csv(sorted_items, out_path)
    else:
        write_csv([], out_path)  # только заголовок

    # вывод резюме в консоль
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генерация отчёта по тексту")
    parser.add_argument("--in", dest="in_path", default="data/input.txt", help="путь к входному файлу")
    parser.add_argument("--out", dest="out_path", default="data/report.csv", help="путь к выходному файлу")
    parser.add_argument("--encoding", default="utf-8", help="кодировка входного файла")
    args = parser.parse_args()

    try:
        make_report(Path(args.in_path), Path(args.out_path), args.encoding)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
