import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    # проверки
    if not json_path.exists():
        raise FileNotFoundError(f"файл не найден")
    if json_path.suffix.lower() != ".json":
        raise ValueError(f"ошибка: ожидается JSON-файл, а получен {json_path.suffix}")

    # читаем JSON
    with json_path.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"ошибка чтения json: {e}")

    # проверка содержимого
    if not data or not isinstance(data, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура (ожидается список словарей)")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    # определяем заголовки (ключи)
    # можно отсортировать по первому объекту или по алфавиту
    fieldnames = sorted({key for obj in data for key in obj.keys()})

    # запись CSV
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    # проверки
    if not csv_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Ошибка: ожидается CSV-файл, а получен {csv_path.suffix}")

    # читаем CSV
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV-файл не содержит заголовка")
        data = list(reader)

    if not data:
        raise ValueError("Пустой CSV-файл")

    # записываем JSON
    json_path.parent.mkdir(parents=True, exist_ok=True)
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    print("всё норм")