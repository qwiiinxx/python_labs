"""
Модуль с реализацией односвязного списка (Singly Linked List).
"""
from typing import Any, Iterator


class Node:
    """
    Узел односвязного списка.
    
    Attributes:
        value: Значение элемента
        next: Ссылка на следующий узел или None, если это последний узел.
    """
    
    def __init__(self, value: Any, next: 'Node | None' = None):
        """
        Инициализация узла
 ё
        """
        self.value: Any = value
        self.next: 'Node | None' = next
    
    def __repr__(self) -> str:
        """Строковое представление узла."""
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    Односвязный список, состоящий из узлов Node.
    
    Использует tail для оптимизации операций добавления в конец за O(1)

    """
    
    def __init__(self):
        """Инициализация пустого списка."""
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        """
        Добавить элемент в конец списка
        
        Сложность: O(1) благодаря использованию tail

        """
        new_node = Node(value)
        
        if self.head is None:
            # Список пуст - новый узел становится и головой, и хвостом
            self.head = new_node
            self.tail = new_node
        else:
            # Добавляем в конец, обновляем tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """
        Добавить элемент в начало списка
        
        Сложность: O(1).
 
        """
        new_node = Node(value, next=self.head)
        self.head = new_node
        
        # Если список был пуст, новый узел также является tail
        if self.tail is None:
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """
        Вставить элемент по индексу
        
        Сложность: O(n) в худшем случае (вставка в середину)

        """
        if idx < 0:
            raise IndexError(f"Index {idx} is out of range. Negative indices are not supported")
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        if idx > self._size:
            raise IndexError(f"Index {idx} is out of range. List size is {self._size}.")
        
        # Вставляем в середину
        current = self.head
        for _ in range(idx - 1):
            if current is None:
                raise IndexError(f"Index {idx} is out of range.")
            current = current.next
        
        if current is None:
            raise IndexError(f"Index {idx} is out of range.")
        
        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1
    
    def remove_at(self, idx: int) -> None:
        """
        Удалить элемент по индексу.
        
        Сложность: O(n) в худшем случае.
        
        Args:
            idx: Индекс элемента для удаления.
            
        Raises:
            IndexError: Если индекс вне диапазона или список пуст.
        """
        if self._size == 0:
            raise IndexError("Cannot remove from empty list")
        
        if idx < 0:
            raise IndexError(f"Index {idx} is out of range. Negative indices are not supported.")
        
        if idx >= self._size:
            raise IndexError(f"Index {idx} is out of range. List size is {self._size}.")
        
        # Удаляем первый элемент
        if idx == 0:
            self.head = self.head.next
            # Если список стал пуст, обновляем tail
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        # Удаляем элемент из середины или конца
        current = self.head
        for _ in range(idx - 1):
            if current is None:
                raise IndexError(f"Index {idx} is out of range.")
            current = current.next
        
        if current is None or current.next is None:
            raise IndexError(f"Index {idx} is out of range.")
        
        # Если удаляем последний элемент, обновляем tail
        if current.next == self.tail:
            self.tail = current
        
        current.next = current.next.next
        self._size -= 1
    
    def remove(self, value: Any) -> None:
        """
        Удалить первое вхождение значения.
        
        Сложность: O(n).
        
        Args:
            value: Значение для удаления.
            
        Raises:
            ValueError: Если значение не найдено в списке.
        """
        if self._size == 0:
            raise ValueError(f"Value {value} not found in list")
        
        # Удаляем первый элемент
        if self.head is not None and self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        # Ищем элемент в середине или конце
        current = self.head
        while current is not None and current.next is not None:
            if current.next.value == value:
                # Если удаляем последний элемент, обновляем tail
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next
        
        raise ValueError(f"Value {value} not found in list")
    
    def __iter__(self) -> Iterator[Any]:
        """
        Возвращает итератор по значениям в списке (от головы к хвосту).
        
        Yields:
            Значения узлов в порядке от головы к хвосту.
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в списке.
        
        Сложность: O(1).
        
        Returns:
            Количество элементов в списке.
        """
        return self._size
    
    def __repr__(self) -> str:
        """
        Возвращает строковое представление списка.
        
        Returns:
            Строковое представление вида: SinglyLinkedList([1, 2, 3])
        """
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def __str__(self) -> str:
        """
        Возвращает красивое текстовое представление структуры списка.
        
        Пример: [A] -> [B] -> [C] -> None
        
        Returns:
            Строковое представление со стрелками.
        """
        if self.head is None:
            return "None"
        
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        
        parts.append("None")
        return " -> ".join(parts)