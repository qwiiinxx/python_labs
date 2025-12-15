"""
Модуль с реализацией базовых структур данных: Stack и Queue.
"""
from collections import deque
from typing import Any


class Stack:
    """
    Структура данных «стек» (LIFO - Last In, First Out).
    
    Реализована на базе list, где вершина стека — последний элемент списка.
    Все операции имеют сложность O(1) амортизированно.
    
    Пример использования:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.peek()  # 2
        2
        >>> stack.pop()  # 2
        2
        >>> stack.pop()  # 1
        1
    """
    
    def __init__(self):
        """Инициализация пустого стека."""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """
        Добавить элемент на вершину стека.
        
        Сложность: O(1) амортизированно.
        
        Args:
            item: Элемент для добавления в стек.
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """
        Снять верхний элемент стека и вернуть его.
        
        Сложность: O(1).
        
        Returns:
            Верхний элемент стека.
            
        Raises:
            IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self._data.pop()
    
    def peek(self) -> Any | None:
        """
        Вернуть верхний элемент без удаления.
        
        Сложность: O(1).
        
        Returns:
            Верхний элемент стека или None, если стек пуст.
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """
        Проверить, пуст ли стек.
        
        Сложность: O(1).
        
        Returns:
            True, если стек пуст, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.
        
        Сложность: O(1).
        
        Returns:
            Количество элементов в стеке.
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        """Строковое представление стека."""
        return f"Stack({self._data})"


class Queue:
    """
    Структура данных «очередь» (FIFO - First In, First Out).
    
    Реализована на базе collections.deque для эффективных операций
    добавления и удаления элементов. Все операции имеют сложность O(1).
    
    Пример использования:
        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.peek()  # 1
        1
        >>> queue.dequeue()  # 1
        1
        >>> queue.dequeue()  # 2
        2
    """
    
    def __init__(self):
        """Инициализация пустой очереди."""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        Добавить элемент в конец очереди.
        
        Сложность: O(1).
        
        Args:
            item: Элемент для добавления в очередь.
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """
        Взять элемент из начала очереди и вернуть его.
        
        Сложность: O(1).
        
        Returns:
            Первый элемент очереди.
            
        Raises:
            IndexError: Если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self._data.popleft()
    
    def peek(self) -> Any | None:
        """
        Вернуть первый элемент без удаления.
        
        Сложность: O(1).
        
        Returns:
            Первый элемент очереди или None, если очередь пуста.
        """
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """
        Проверить, пуста ли очередь.
        
        Сложность: O(1).
        
        Returns:
            True, если очередь пуста, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди.
        
        Сложность: O(1).
        
        Returns:
            Количество элементов в очереди.
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        """Строковое представление очереди."""
        return f"Queue({list(self._data)})"
