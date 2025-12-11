import csv
from pathlib import Path
from typing import List

from src.lab08.models import Student


class Group:
    """Класс для работы с базой данных студентов в CSV-формате."""

    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, csv_path: str):
        """
        Инициализация группы с путём к CSV-файлу
   
        """
        self.path = Path(csv_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Создаёт файл с заголовком, если его ещё нет"""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self) -> List[dict]:
        """
        Читает все строки из CSV и возвращает как список словарей
        
        """
        if not self.path.exists():
            return []

        with self.path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # Проверяем наличие заголовка
            if reader.fieldnames != self.HEADER:
                raise ValueError(
                    f"Неверный формат CSV: ожидается заголовок {self.HEADER}, "
                    f"получен {reader.fieldnames}"
                )
            return list(reader)

    def _write_all(self, rows: List[dict]) -> None:
        """
        Записывает все строки в CSV

        """
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> List[Student]:
        """
        Возвращает всех студентов в виде списка объектов Student
        
        """
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except (ValueError, TypeError) as e:
                # Пропускаем некорректные записи с предупреждением
                print(f"Пропущена некорректная запись {row}: {e}")
        return students

    def add(self, student: Student) -> None:
        """
        Добавляет нового студента в CSV

        """
        if not isinstance(student, Student):
            raise TypeError("student must be an instance of Student")

        rows = self._read_all()
        student_dict = student.to_dict()
        rows.append(student_dict)
        self._write_all(rows)

    def find(self, substr: str) -> List[dict]:
        """
        Находит студентов по подстроке в ФИО
        
        """
        if not isinstance(substr, str):
            raise TypeError("substr must be a string")
        if not substr.strip():
            raise ValueError("substr must be a non-empty string")
        
        rows = self._read_all()
        return [r for r in rows if substr in r["fio"]]

    def remove(self, fio: str) -> None:
        """
        Удаляет запись(и) с данным ФИО.
        
        """
        if not isinstance(fio, str):
            raise TypeError("fio must be a string")
        if not fio.strip():
            raise ValueError("fio must be a non-empty string")
        
        rows = self._read_all()
        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                break
        self._write_all(rows)

    def update(self, fio: str, **fields) -> bool:
        """
        Обновляет поля существующего студента.
        
        Args:
            fio: ФИО студента для обновления
            **fields: поля для обновления (например, gpa=4.5, group="БИВТ-21-1")
            
        Returns:
            True, если была обновлена хотя бы одна запись, False иначе
        """
        if not isinstance(fio, str):
            raise TypeError("fio must be a string")

        if not fields:
            raise ValueError("Не указаны поля для обновления")

        # Проверяем, что обновляемые поля допустимы
        valid_fields = set(self.HEADER)
        invalid_fields = set(fields.keys()) - valid_fields
        if invalid_fields:
            raise ValueError(f"Недопустимые поля для обновления: {invalid_fields}")

        rows = self._read_all()
        updated = False

        for row in rows:
            if row["fio"] == fio:
                # Обновляем поля
                for key, value in fields.items():
                    row[key] = value
                updated = True

        if updated:
            # Валидируем обновлённые записи, создавая объекты Student
            for row in rows:
                if row["fio"] == fio:
                    try:
                        Student.from_dict(row)
                    except (ValueError, TypeError) as e:
                        raise ValueError(f"Обновление привело к некорректным данным: {e}")

            self._write_all(rows)
            return True

        return False

    def stats(self) -> dict:
        """
        Возвращает статистику по группе студентов.
        
        Returns:
            Словарь со статистикой:
            - count: общее количество студентов
            - min_gpa: минимальный GPA
            - max_gpa: максимальный GPA
            - avg_gpa: средний GPA
            - groups: словарь с количеством студентов по группам
            - top_5_students: топ-5 студентов по GPA
        """
        students = self.list()

        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": [],
            }

        gpa_values = [s.gpa for s in students]
        groups_dict = {}
        for student in students:
            groups_dict[student.group] = groups_dict.get(student.group, 0) + 1

        # Сортируем студентов по GPA (по убыванию) и берём топ-5
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa} for s in sorted_students[:5]
        ]

        return {
            "count": len(students),
            "min_gpa": min(gpa_values),
            "max_gpa": max(gpa_values),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups_dict,
            "top_5_students": top_5,
        }
        