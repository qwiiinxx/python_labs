import csv
from pathlib import Path
from typing import List

from src.lab08.models import Student


class Group:
    """Класс для работы с базой данных студентов в CSV-формате."""

    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        """
        Инициализация группы с путём к CSV-файлу.
        
        Args:
            storage_path: путь к CSV-файлу для хранения данных студентов
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Создаёт файл с заголовком, если его ещё нет."""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self) -> List[dict]:
        """
        Читает все строки из CSV и возвращает их как список словарей.
        
        Returns:
            Список словарей с данными студентов (без заголовка)
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
        Записывает все строки в CSV.
        
        Args:
            rows: список словарей с данными студентов
        """
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> List[Student]:
        """
        Возвращает всех студентов в виде списка объектов Student.
        
        Returns:
            Список объектов Student
        """
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except (ValueError, TypeError) as e:
                # Пропускаем некорректные записи с предупреждением
                print(f"Предупреждение: пропущена некорректная запись {row}: {e}")
        return students

    def add(self, student: Student) -> None:
        """
        Добавляет нового студента в CSV.
        
        Args:
            student: объект Student для добавления
        """
        if not isinstance(student, Student):
            raise TypeError("student must be an instance of Student")

        rows = self._read_all()
        student_dict = student.to_dict()
        rows.append(student_dict)
        self._write_all(rows)

    def find(self, substr: str) -> List[Student]:
        """
        Находит студентов по подстроке в ФИО.
        
        Args:
            substr: подстрока для поиска в поле fio
            
        Returns:
            Список объектов Student, у которых в fio содержится substr
        """
        if not isinstance(substr, str):
            raise TypeError("substr must be a string")

        all_students = self.list()
        return [s for s in all_students if substr.lower() in s.fio.lower()]

    def remove(self, fio: str) -> bool:
        """
        Удаляет запись(и) с данным ФИО.
        
        Args:
            fio: ФИО студента для удаления
            
        Returns:
            True, если была удалена хотя бы одна запись, False иначе
        """
        if not isinstance(fio, str):
            raise TypeError("fio must be a string")

        rows = self._read_all()
        initial_count = len(rows)
        rows = [r for r in rows if r["fio"] != fio]
        
        if len(rows) < initial_count:
            self._write_all(rows)
            return True
        return False

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

