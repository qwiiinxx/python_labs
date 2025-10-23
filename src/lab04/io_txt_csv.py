from pathlib import Path
import csv
from typing import Iterable, Sequence
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(__file__).parent / path  # путь относительно текущего файла
    if not p.exists(): # ошибка если файл не найден
        raise FileNotFoundError(f"файл {p} не найден")
    return p.read_text(encoding=encoding) # чтение файла с любой кодировкой


def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)        


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path) # создали путь
    
    # проверка на одинаковую длину строк
    if rows:
        length = len(rows[0])
        for row in rows:
            if len(row) != length:
                raise ValueError("все строки должны быть одинаковой длины")
        
        if header is not None and len(header) != length:
            raise ValueError(f"длина заголовков ({len(header)}) не совпадает с длиной строк {length}")
            

    with p.open("w", newline="", encoding="utf-8") as f: # открыли 
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)



if __name__ == "__main__":
    # тесты писать прямо здесь
    txt = read_text("../../data/lab04/input.txt")  # должен вернуть строку
    write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV
