from pathlib import Path  # запускать через python3 -m src.lab04.text_report
import sys, os

# === ДОБАВЛЯЕМ КОРЕНЬ ПРОЕКТА В sys.path ===
# Это нужно, чтобы можно было импортировать из src.*
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq


def main():
    # Формируем пути относительно корня проекта
    root = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    input_path = root / "data" / "lab04" / "input.txt"
    output_path = root / "data" / "lab04" / "report.csv"

    # Проверяем существование входного файла
    if not input_path.exists():
        print(f"Файл не найден: {input_path}")
        sys.exit(1)

    # Читаем текст
    text = read_text(input_path)
    if not text.strip():
        print("Пустой файл — создаю CSV только с заголовком.")
        write_csv([], output_path, header=("word", "count"))
        return

    # Обрабатываем текст
    norm_text = normalize(text)
    tokens = tokenize(norm_text)
    freqs = count_freq(tokens)

    # Сортируем результат по убыванию количества, затем по алфавиту
    sorted_rows = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))

    # Пишем отчёт
    write_csv(sorted_rows, output_path, header=("word", "count"))

    # Печатаем краткий итог
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freqs)}")
    print("Топ-5:", sorted_rows[:5])


if __name__ == "__main__":
    main()
