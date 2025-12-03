from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from .models import Student


def students_to_json(students: Iterable[Student], path: str | Path) -> None:
    """
    Сохранить список студентов в JSON‑файл.

    Формат файла — JSON-массив словарей, как из Student.to_dict().
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    data = [s.to_dict() for s in students]
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> List[Student]:
    """
    Прочитать JSON‑файл и вернуть список объектов Student.

    Выполняется базовая валидация структуры JSON, далее срабатывает
    валидация в самом классе Student.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"file not found: {p}")

    with p.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON file: {exc}") from exc

    if not isinstance(data, list):
        raise ValueError("JSON root must be a list of objects")

    students: List[Student] = []
    for item in data:
        students.append(Student.from_dict(item))

    return students


