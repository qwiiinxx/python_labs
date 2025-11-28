# Лабораторная № 7
## **pytest + black**
#### Устанавливаем ```pip install pytest```
## Задание А
### Запуск через: `pytest -v tests/test_text.py`
```python
from src.lib.text import normalize, tokenize, count_freq, top_n
import pytest

@pytest.mark.parametrize("text, expected", [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ])  
def test_normalize(text, expected):
    assert normalize(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("привет, мир!", ["привет", "мир"]),
    ("Hello, World!!!", ["Hello", "World"]),
    ("по-настоящему круто", ["по-настоящему", "круто"]),
    ("2025 год!", ["2025", "год"]),
    ("emoji 😀 не слово!", ["emoji", "не", "слово"]),
])
def test_tokenize(text, expected):
    assert tokenize(text) == expected


@pytest.mark.parametrize("tokens, expected", [
    (["c", "b", "a", "c", "b", "a"], {"a":2, "b":2, "c":2}),
    (["bb", "aa", "bb", "aa", "cc"], {"aa":2, "bb":2, "cc":1}),
    (["c","b","c","c","b","a"], {"c":3, "b":2, "a":1}),
])
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize("freq, n,expected", [
    ({"c":2, "b":2, "a":2}, 3, [("a", 2), ("b", 2), ("c", 2)]),
    ({"bb":2, "aa":2, "cc":1}, 2,[("aa", 2), ("bb", 2)]),
    ({"x":5, "y":5, "a":5}, 3, [("a", 5), ("x", 5), ("y", 5)]),
    ({"x":5, "y":5, "a":5}, 1, [("a", 5)]),
])
def test_top_n(freq, n, expected):
    assert top_n(freq, n=n) == expected
```
Pytest:
![Картинка 1](../../images/lab07/img01.png)
---
![Картинка 2](../../images/lab07/img02.png)
---
![Картинка 3](../../images/lab07/img03.png)
---
![Картинка 4](../../images/lab07/img04.png)
---

## Задание В
### Запуск через ```pytest -v tests/test_json_csv.py```
## Позитивные сценарии
```python
import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"

    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]

    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    
    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert set(rows[0].keys()) == {"name", "age"}
    assert rows[0]["name"] == "Alice"
    assert rows[1]["age"] == "25"



def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    data = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]

    
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(data)

    
    csv_to_json(str(src), str(dst))


    with dst.open(encoding="utf-8") as f:
        rows = json.load(f)

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())
    assert rows == data
```
![Картинка 5](../../images/lab07/img05.png)

---

### Негативные тесты для `json_to_csv` и `csv_to_json`

#### Выполненные задачи
**2. Добавлены негативные тесты для `json_to_csv`:**
   - `test_json_to_csv_file_not_found` - проверка `FileNotFoundError` при несуществующем файле
   - `test_json_to_csv_wrong_extension` - проверка `ValueError` при неправильном расширении
   - `test_json_to_csv_empty_file` - проверка `ValueError` при пустом файле
   - `test_json_to_csv_invalid_json` - проверка `ValueError` при некорректном JSON
   - `test_json_to_csv_empty_list` - проверка `ValueError` при пустом списке в JSON
   - `test_json_to_csv_not_list` - проверка `ValueError` когда JSON не является списком
   - `test_json_to_csv_not_dicts` - проверка `ValueError` когда элементы не являются словарями

**3. Негативные тесты для `csv_to_json`:**
   - `test_csv_to_json_file_not_found` - проверка `FileNotFoundError` при несуществующем файле
   - `test_csv_to_json_wrong_extension` - проверка `ValueError` при неправильном расширении
   - `test_csv_to_json_empty_file` - проверка `ValueError` при пустом файле
   - `test_csv_to_json_no_header` - проверка `ValueError` при CSV только с одной строкой данных
   - `test_csv_to_json_only_header` - проверка `ValueError` при CSV только с заголовком без данных

**4. Использованные инструменты:**
   - Фикстура `tmp_path` из pytest для работы с временными файлами
   - `pytest.raises()` для проверки выброса исключений
   - Параметр `match` для проверки текста сообщения об ошибке

#### Результаты тестирования

**Запуск тестов:**
```bash
pytest -v tests/test_json_csv.py
```

**Результат:**
```
============================= test session starts ==============================
platform darwin -- Python 3.13.7, pytest-9.0.1, pluggy-1.6.0
collected 14 items

tests/test_json_csv.py ..............                                    [100%]

============================== 14 passed in 0.02s ==============================
```

**Статистика:**
- Всего тестов: **14**
- Позитивных тестов: **2** (уже существовали)
- Негативных тестов: **12** (добавлено)
- Успешно пройдено: **14/14** (100%)

**Проверка исключений:** Использован контекстный менеджер `pytest.raises()` с параметром `match` для проверки не только типа исключения, но и содержания сообщения об ошибке.

**Покрытие граничных случаев:** Тесты покрывают различные граничные случаи:
   - Отсутствие файла
   - Пустые файлы
   - Некорректные форматы данных
   - Неправильные структуры данных
   - Неправильные расширения файлов
