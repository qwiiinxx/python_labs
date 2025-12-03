from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Dict


@dataclass
class Student:
    """
    Модель студента для ЛР8.

    Поля:
    - fio: ФИО студента (строка)
    - birthdate: дата рождения в формате YYYY-MM-DD
    - group: группа, например "SE-01"
    - gpa: средний балл от 0 до 5 включительно
    """

    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self) -> None:
        """Валидация полей после инициализации dataclass."""

        # ФИО и группа не должны быть пустыми
        if not isinstance(self.fio, str) or not self.fio.strip():
            raise ValueError("fio must be a non-empty string")
        if not isinstance(self.group, str) or not self.group.strip():
            raise ValueError("group must be a non-empty string")

        # Проверяем формат даты рождения: YYYY-MM-DD
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except (TypeError, ValueError) as exc:
            raise ValueError("birthdate must be in format YYYY-MM-DD") from exc

        # gpa должно быть числом в диапазоне [0, 5]
        try:
            self.gpa = float(self.gpa)
        except (TypeError, ValueError) as exc:
            raise ValueError("gpa must be a number") from exc

        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        """
        Вернуть количество полных лет студента.

        Использует сегодняшнюю дату и дату рождения (birthdate).
        """
        born = date.fromisoformat(self.birthdate)
        today = date.today()
        years = today.year - born.year
        if (today.month, today.day) < (born.month, born.day):
            years -= 1
        return years

    def to_dict(self) -> Dict[str, Any]:
        """
        Сериализовать объект Student в словарь, готовый для JSON.
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        """
        Создать экземпляр Student из словаря.

        Ожидаются ключи: fio, birthdate, group, gpa.
        Валидация выполняется в __post_init__.
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dict")

        return cls(
            fio=data.get("fio", ""),
            birthdate=data.get("birthdate", ""),
            group=data.get("group", ""),
            gpa=data.get("gpa", 0.0),
        )

    def __str__(self) -> str:
        """
        Красивый человеко‑читаемый вывод.
        """
        return f"{self.fio} (гр. {self.group}), GPA {self.gpa:.2f}, {self.age()} лет"

