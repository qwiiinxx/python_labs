"""
Модуль с реализацией базовых структур данных: Stack и Queue.
"""
from collections import deque
from typing import Any


class Stack:
    """
    LIFO - Last In, First Out
    
    Реализована на базе list, где вершина стека — последний элемент списка.
    Все операции имеют сложность O(1) амортизированно.
    
    """
    
    def __init__(self):
        """Инициализация пустого стека"""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """
        Добавить элемент на вершину стека
        
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """
        Снять верхний элемент стека и вернуть его
        
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self._data.pop()
    
    def peek(self) -> Any | None:
        """
        Вернуть верхний элемент без удаления.
        
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """
        Проверить на пустоту
        
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке
     
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        """Строковое представление стека."""
        return f"Stack({self._data})"


class Queue:
    """
    FIFO - First In, First Out
    
    Реализована на базе collections.deque для эффективных операций
    добавления и удаления элементов. Все операции имеют сложность O(1).
    
    """
    
    def __init__(self):
        """Инициализация пустой очереди"""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        Добавить элемент в конец очереди.
        
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """
        Взять элемент из начала очереди и вернуть его.

        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self._data.popleft()
    
    def peek(self) -> Any | None:
        """
        Вернуть первый элемент без удаления.
        
        """
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """
        Проверить, пуста ли очередь
        

        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди
        
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        """Строковое представление очереди."""
        return f"Queue({list(self._data)})"
