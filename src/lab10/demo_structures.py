"""
Демонстрация использования Stack и Queue.
Запуск: python -m src.lab10.demo_structures
"""
from src.lab10.structures import Stack, Queue


def demo_stack():
    """Демонстрация работы со стеком."""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ STACK")
    print("=" * 50)
    
    stack = Stack()
    print(f"Создан пустой стек: {stack}")
    print(f"Стек пуст? {stack.is_empty()}")
    print()
    
    # Добавление элементов
    print("Добавляем элементы: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Состояние стека: {stack}")
    print(f"Размер стека: {len(stack)}")
    print(f"Верхний элемент (peek): {stack.peek()}")
    print()
    
    # Удаление элементов
    print("Удаляем элементы из стека:")
    while not stack.is_empty():
        top = stack.pop()
        print(f"  Извлечён элемент: {top}, осталось элементов: {len(stack)}")
    
    print(f"Стек пуст? {stack.is_empty()}")
    print()


def demo_queue():
    """Демонстрация работы с очередью."""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ QUEUE")
    print("=" * 50)
    
    queue = Queue()
    print(f"Создана пустая очередь: {queue}")
    print(f"Очередь пуста? {queue.is_empty()}")
    print()
    
    # Добавление элементов
    print("Добавляем элементы: 'первый', 'второй', 'третий'")
    queue.enqueue("первый")
    queue.enqueue("второй")
    queue.enqueue("третий")
    print(f"Состояние очереди: {queue}")
    print(f"Размер очереди: {len(queue)}")
    print(f"Первый элемент (peek): {queue.peek()}")
    print()
    
    # Удаление элементов
    print("Удаляем элементы из очереди:")
    while not queue.is_empty():
        first = queue.dequeue()
        print(f"  Извлечён элемент: {first}, осталось элементов: {len(queue)}")
    
    print(f"Очередь пуста? {queue.is_empty()}")
    print()


def demo_error_handling():
    """Демонстрация обработки ошибок."""
    print("=" * 50)
    print("ОБРАБОТКА ОШИБОК")
    print("=" * 50)
    
    # Попытка извлечения из пустого стека
    print("Попытка pop() из пустого стека:")
    empty_stack = Stack()
    try:
        empty_stack.pop()
    except IndexError as e:
        print(f"  Поймано исключение: {e}")
    print()
    
    # Попытка извлечения из пустой очереди
    print("Попытка dequeue() из пустой очереди:")
    empty_queue = Queue()
    try:
        empty_queue.dequeue()
    except IndexError as e:
        print(f"  Поймано исключение: {e}")
    print()
    
    # peek() на пустых структурах
    print("peek() на пустых структурах:")
    print(f"  Пустой стек: {empty_stack.peek()}")
    print(f"  Пустая очередь: {empty_queue.peek()}")


def main():
    """Основная функция для запуска демонстраций."""
    demo_stack()
    demo_queue()
    demo_error_handling()


if __name__ == "__main__":
    main()