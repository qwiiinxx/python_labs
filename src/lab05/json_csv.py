import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path = Path()
    csv_path = Path()

    # проверка на существование файла
    if not json_path.exists():
        raise FileNotFoundError
    if not csv_path.exists():
        raise FileNotFoundError
    
    # чтение json файла
    with open('people_from_csv', 'r', encoding='utf-8') as f:
        text = f.read()

        # проверка на пустоту
        if text is None:
            raise ValueError
        
        # проверка на тип файла 'json'
        if json_path.suffix.lower() != ".json":
            raise ValueError(f"ошибка: ожидается json файл")
    data = json.loads(text)

    # запись в csv
    with open('people_from_json', 'w', 'newline=') as csvfile:
        fieldnames = ['name', 'age', 'id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in text:
            if text is None:
                raise ValueError
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path = Path()
    json_path = Path()

    # проверка на существование файла
    if not json_path.exists():
        raise FileNotFoundError
    if not csv_path.exists():
        raise FileNotFoundError
    
    