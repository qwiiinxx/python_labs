"""
Бенчмарки производительности для Stack, Queue и SinglyLinkedList.
Запуск: python -m src.lab10.benchmarks
"""
import time
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


def benchmark_push(n: int) -> dict:
    """Бенчмарк добавления элементов."""
    results = {}
    
    # Stack
    stack = Stack()
    start = time.perf_counter()
    for i in range(n):
        stack.push(i)
    results['Stack.push()'] = time.perf_counter() - start
    
    # Queue
    queue = Queue()
    start = time.perf_counter()
    for i in range(n):
        queue.enqueue(i)
    results['Queue.enqueue()'] = time.perf_counter() - start
    
    # SinglyLinkedList
    lst = SinglyLinkedList()
    start = time.perf_counter()
    for i in range(n):
        lst.append(i)
    results['SinglyLinkedList.append()'] = time.perf_counter() - start
    
    return results


def benchmark_pop(n: int) -> dict:
    """Бенчмарк удаления элементов."""
    results = {}
    
    # Stack
    stack = Stack()
    for i in range(n):
        stack.push(i)
    start = time.perf_counter()
    for _ in range(n):
        stack.pop()
    results['Stack.pop()'] = time.perf_counter() - start
    
    # Queue
    queue = Queue()
    for i in range(n):
        queue.enqueue(i)
    start = time.perf_counter()
    for _ in range(n):
        queue.dequeue()
    results['Queue.dequeue()'] = time.perf_counter() - start
    
    # SinglyLinkedList (удаление из начала)
    lst = SinglyLinkedList()
    for i in range(n):
        lst.append(i)
    start = time.perf_counter()
    for _ in range(n):
        lst.remove_at(0)
    results['SinglyLinkedList.remove_at(0)'] = time.perf_counter() - start
    
    return results


def benchmark_insert(n: int) -> dict:
    """Бенчмарк вставки в начало."""
    results = {}
    
    # Stack (не поддерживает вставку в начало, только push)
    stack = Stack()
    start = time.perf_counter()
    for i in range(n):
        stack.push(i)
    results['Stack.push() (эквивалент)'] = time.perf_counter() - start
    
    # Queue (не поддерживает вставку в начало напрямую)
    queue = Queue()
    start = time.perf_counter()
    for i in range(n):
        queue.enqueue(i)
    results['Queue.enqueue() (эквивалент)'] = time.perf_counter() - start
    
    # SinglyLinkedList (вставка в начало)
    lst = SinglyLinkedList()
    start = time.perf_counter()
    for i in range(n):
        lst.prepend(i)
    results['SinglyLinkedList.prepend()'] = time.perf_counter() - start
    
    return results


def benchmark_access(n: int) -> dict:
    """Бенчмарк доступа к элементам."""
    results = {}
    
    # Stack.peek() (доступ к последнему элементу)
    stack = Stack()
    for i in range(n):
        stack.push(i)
    start = time.perf_counter()
    for _ in range(n):
        stack.peek()
    results['Stack.peek()'] = time.perf_counter() - start
    
    # Queue.peek() (доступ к первому элементу)
    queue = Queue()
    for i in range(n):
        queue.enqueue(i)
    start = time.perf_counter()
    for _ in range(n):
        queue.peek()
    results['Queue.peek()'] = time.perf_counter() - start
    
    # SinglyLinkedList (доступ по индексу - требует итерацию)
    lst = SinglyLinkedList()
    for i in range(n):
        lst.append(i)
    start = time.perf_counter()
    # Симулируем доступ к последнему элементу через итерацию
    for _ in range(min(n, 100)):  # Ограничиваем для больших n
        list(lst)[-1]
    results['SinglyLinkedList (итерация до конца)'] = time.perf_counter() - start
    
    return results


def benchmark_iteration(n: int) -> dict:
    """Бенчмарк итерации по всем элементам."""
    results = {}
    
    # Stack (преобразование в list и обратно)
    stack = Stack()
    for i in range(n):
        stack.push(i)
    start = time.perf_counter()
    for _ in range(10):  # Несколько итераций для точности
        list(stack._data)
    results['Stack (внутренний list)'] = (time.perf_counter() - start) / 10
    
    # Queue
    queue = Queue()
    for i in range(n):
        queue.enqueue(i)
    start = time.perf_counter()
    for _ in range(10):
        list(queue._data)
    results['Queue (внутренний deque)'] = (time.perf_counter() - start) / 10
    
    # SinglyLinkedList
    lst = SinglyLinkedList()
    for i in range(n):
        lst.append(i)
    start = time.perf_counter()
    for _ in range(10):
        list(lst)
    results['SinglyLinkedList.__iter__()'] = (time.perf_counter() - start) / 10
    
    return results


def print_results(title: str, results: dict, n: int):
    """Вывести результаты бенчмарка в читаемом формате."""
    print(f"\n{'=' * 70}")
    print(f"{title} (n = {n:,})")
    print(f"{'=' * 70}")
    
    # Сортируем по времени
    sorted_results = sorted(results.items(), key=lambda x: x[1])
    
    min_time = sorted_results[0][1]
    
    for operation, elapsed in sorted_results:
        ratio = elapsed / min_time if min_time > 0 else 1.0
        bar = "█" * int(ratio * 30)
        print(f"{operation:45s} {elapsed:8.6f} сек  {bar} ({ratio:.2f}x)")


def main():
    """Основная функция для запуска всех бенчмарков."""
    print("=" * 70)
    print("БЕНЧМАРКИ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 70)
    print("\nСравнение производительности Stack, Queue и SinglyLinkedList")
    
    # Размеры для тестирования
    sizes = [100, 1000, 10000]
    
    for n in sizes:
        # Добавление элементов
        results = benchmark_push(n)
        print_results("ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ", results, n)
        
        # Удаление элементов
        results = benchmark_pop(n)
        print_results("УДАЛЕНИЕ ЭЛЕМЕНТОВ", results, n)
        
        # Вставка в начало
        results = benchmark_insert(n)
        print_results("ВСТАВКА В НАЧАЛО", results, n)
        
        # Доступ к элементам
        results = benchmark_access(min(n, 1000))  # Ограничиваем для SinglyLinkedList
        print_results("ДОСТУП К ЭЛЕМЕНТАМ", results, min(n, 1000))
        
        # Итерация
        results = benchmark_iteration(n)
        print_results("ИТЕРАЦИЯ ПО ВСЕМ ЭЛЕМЕНТАМ", results, n)
    
    print("\n" + "=" * 70)
    print("ВЫВОДЫ:")
    print("=" * 70)
    print("""
1. Stack и Queue (на базе list/deque) обычно быстрее благодаря 
   низкоуровневым оптимизациям Python.

2. SinglyLinkedList имеет большие накладные расходы из-за работы 
   с указателями и cache misses.

3. Для большинства практических задач в Python лучше использовать 
   встроенные структуры (list, deque).

4. Связные списки полезны для обучения и понимания структур данных,
   а также когда важна вставка/удаление в начало за O(1).
    """)


if __name__ == "__main__":
    main()