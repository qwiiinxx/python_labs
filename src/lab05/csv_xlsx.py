from pathlib import Path
import csv
from openpyxl import Workbook
import os


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    # проверка входного файла
    if not csv_path.exists():
        raise FileNotFoundError(f"файл не найден: {csv_path}")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError("ошибка: ожидается входной файл с расширением .csv")

    # проверка выходного файла
    if xlsx_path.suffix.lower() != ".xlsx":
        raise ValueError("ошибка: выходной файл должен иметь расширение .xlsx")

    # чтение CSV
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("ошибка: CSV пустой")
    if not any(rows[0]):
        raise ValueError("ошибка: CSV не содержит заголовков")

    # Создание Excel-файла
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # автоширина колонок
    for column_cells in ws.columns:
        max_length = 0
        column_letter = column_cells[0].column_letter  # A, B, C, ...
        for cell in column_cells:
            value = str(cell.value) if cell.value is not None else ""
            max_length = max(max_length, len(value))
        adjusted_width = max(max_length + 2, 8)  # минимум 8 символов
        ws.column_dimensions[column_letter].width = adjusted_width

    os.makedirs(os.path.dirname(xlsx_path), exist_ok=True)
    # сохранение
    wb.save(xlsx_path)


if __name__ == "__main__":
    csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
    print("всё норм")
