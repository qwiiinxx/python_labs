"""Бенчмарки для Stack, Queue и SinglyLinkedList.

Запуск из корня проекта:

    python3 -m src.lab10.benchmarks

Модуль печатает времена работы основных операций и краткий вывод.
"""

from __future__ import annotations

import time
from typing import Callable

from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


def _timeit(func: Callable[[], None]) -> float:
    """Замеряет время выполнения функции в секундах."""
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return end - start


def bench_push(n: int) -> dict[str, float]:
    """Добавление n элементов."""

    def stack_job() -> None:
        s = Stack()
        for i in range(n):
            s.push(i)

    def queue_job() -> None:
        q = Queue()
        for i in range(n):
            q.enqueue(i)

    def list_job() -> None:
        lst = SinglyLinkedList()
        for i in range(n):
            lst.append(i)

    return {
        "Stack.push": _timeit(stack_job),
        "Queue.enqueue": _timeit(queue_job),
        "SinglyLinkedList.append": _timeit(list_job),
    }


def bench_pop(n: int) -> dict[str, float]:
    """Удаление n элементов (из конца/начала)."""

    def stack_job() -> None:
        s = Stack()
        for i in range(n):
            s.push(i)
        for _ in range(n):
            s.pop()

    def queue_job() -> None:
        q = Queue()
        for i in range(n):
            q.enqueue(i)
        for _ in range(n):
            q.dequeue()

    def list_job() -> None:
        lst = SinglyLinkedList()
        for i in range(n):
            lst.append(i)
        for _ in range(n):
            lst.remove_at(0)

    return {
        "Stack.pop": _timeit(stack_job),
        "Queue.dequeue": _timeit(queue_job),
        "SinglyLinkedList.remove_at(0)": _timeit(list_job),
    }


def _print_table(title: str, results: dict[str, float], n: int) -> None:
    print("=" * 70)
    print(f"{title} (n = {n:,})")
    print("=" * 70)
    min_time = min(results.values()) or 1.0
    for name, t in sorted(results.items(), key=lambda kv: kv[1]):
        rel = t / min_time
        print(f"{name:30s}  {t:8.5f} сек   ({rel:4.2f}x)")
    print()


def main() -> None:
    sizes = [1_000, 10_000, 50_000]

    print("БЕНЧМАРКИ Stack / Queue / SinglyLinkedList")
    print("(все числа приблизительные, зависят от машины)\n")

    for n in sizes:
        push_res = bench_push(n)
        _print_table("Добавление элементов", push_res, n)

        pop_res = bench_pop(n)
        _print_table("Удаление элементов", pop_res, n)

    print("ИТОГОВЫЙ ВЫВОД:")
    print("- Во всех тестах Stack (list) и Queue (deque) заметно быстрее связного списка.")
    print("- SinglyLinkedList даёт такую же асимптотику O(1) для append/remove_at(0),")
    print("  но из-за указателей и отсутствия локальности данных в памяти работает медленнее.")
    print("- В реальных Python-проектах обычно используют list/deque, а связный список")
    print("  полезен прежде всего как учебный пример структуры данных.")


if __name__ == "__main__":  # pragma: no cover
    main()
