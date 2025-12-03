## Лабораторная работа 8 — ООП в Python: @dataclass Student, методы и сериализация

### Цель работы

Научиться описывать модели данных с помощью `@dataclass`, реализовывать методы и валидацию,
а также выполнять сериализацию/десериализацию объектов в формат JSON.

---

### Класс `Student` (`models.py`)

```python
from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Student:
    fio: str          # ФИО студента
    birthdate: str    # дата рождения в формате YYYY-MM-DD
    group: str        # группа, например "SE-01"
    gpa: float        # средний балл 0..5

    def __post_init__(self) -> None:
        # валидация ФИО и группы
        ...

    def age(self) -> int:
        # количество полных лет
        ...

    def to_dict(self) -> dict:
        # словарь для JSON
        ...

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        # создание из словаря
        ...

    def __str__(self) -> str:
        # человеко‑читаемое представление
        ...
```

**Валидация в `__post_init__`:**

- **формат даты** строго `YYYY-MM-DD` (`datetime.strptime(self.birthdate, "%Y-%m-%d")`)
- **диапазон среднего балла** `0 ≤ gpa ≤ 5` (при несоответствии выбрасывается `ValueError`)

Метод `age()` использует `date.today()` и дату рождения и возвращает количество **полных лет**.

Методы `to_dict()` / `from_dict()` позволяют преобразовывать объект в словарь и обратно,
что удобно для JSON‑сериализации.

Метод `__str__()` возвращает строку вида:

```text
Иванов Иван Иванович (гр. SE-01), GPA 4.25, 20 лет
```

---

### Модуль `serialize.py`

```python
from pathlib import Path
from .models import Student


def students_to_json(students: list[Student], path: str | Path) -> None:
    # сериализация списка студентов в JSON-файл
    ...


def students_from_json(path: str | Path) -> list[Student]:
    # чтение JSON-файла и создание списка Student
    ...
```

- **`students_to_json`**: принимает список объектов `Student`, вызывает `to_dict()` и
  сохраняет JSON‑массив в указанный файл.
- **`students_from_json`**: читает JSON‑массив словарей, для каждого словаря вызывает
  `Student.from_dict`, таким образом выполняя и валидацию данных.

---

### Примеры JSON‑файлов

`data/lab08/students_input.json`:

```json
[
  {
    "fio": "Иванов Иван Иванович",
    "birthdate": "2004-05-12",
    "group": "SE-01",
    "gpa": 4.5
  },
  {
    "fio": "Петров Петр Петрович",
    "birthdate": "2003-09-30",
    "group": "SE-02",
    "gpa": 4.9
  }
]
```

`data/lab08/students_output.json` (результат работы `students_to_json` — структура такая же,
значения могут совпадать или отличаться в зависимости от входных данных):

```json
[
  {
    "fio": "Иванов Иван Иванович",
    "birthdate": "2004-05-12",
    "group": "SE-01",
    "gpa": 4.5
  },
  {
    "fio": "Петров Петр Петрович",
    "birthdate": "2003-09-30",
    "group": "SE-02",
    "gpa": 4.9
  }
]
```

---

### Примеры запуска

Запуск из корня проекта:

```bash
python -m src.lab08.serialize
```

Пример небольшого скрипта (можно выполнять из интерактивной консоли Python):

```python
from pathlib import Path
from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json

root = Path(".")
in_path = root / "data" / "lab08" / "students_input.json"
out_path = root / "data" / "lab08" / "students_output.json"

# читаем студентов из входного JSON
students = students_from_json(in_path)

for s in students:
    print(s)          # печать с помощью __str__()
    print(s.age())    # возраст

# сохраняем (например, после каких‑то изменений)
students_to_json(students, out_path)
```


