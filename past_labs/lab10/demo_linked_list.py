"""
Демонстрация использования SinglyLinkedList.
Запуск: python -m src.lab10.demo_linked_list
"""
from src.lab10.linked_list import SinglyLinkedList


def demo_basic_operations():
    """Демонстрация базовых операций."""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ SINGLY LINKED LIST")
    print("=" * 50)
    
    lst = SinglyLinkedList()
    print(f"Создан пустой список: {repr(lst)}")
    print(f"Размер списка: {len(lst)}")
    print(f"Красивое представление: {str(lst)}")
    print()
    
    # Добавление в конец
    print("Добавляем элементы в конец: 1, 2, 3")
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"Список: {lst}")
    print(f"Красивое представление: {str(lst)}")
    print(f"Размер: {len(lst)}")
    print()
    
    # Добавление в начало
    print("Добавляем элемент в начало: 0")
    lst.prepend(0)
    print(f"Список: {lst}")
    print(f"Красивое представление: {str(lst)}")
    print(f"Размер: {len(lst)}")
    print()
    
    # Вставка по индексу
    print("Вставляем элемент по индексу 2: 1.5")
    lst.insert(2, 1.5)
    print(f"Список: {lst}")
    print(f"Красивое представление: {str(lst)}")
    print()


def demo_removal():
    """Демонстрация удаления элементов."""
    print("=" * 50)
    print("УДАЛЕНИЕ ЭЛЕМЕНТОВ")
    print("=" * 50)
    
    lst = SinglyLinkedList()
    for i in range(1, 6):
        lst.append(i)
    
    print(f"Исходный список: {lst}")
    print(f"Красивое представление: {str(lst)}")
    print()
    
    # Удаление по индексу
    print("Удаляем элемент по индексу 2 (значение 3):")
    lst.remove_at(2)
    print(f"Список: {lst}")
    print(f"Красивое представление: {str(lst)}")
    print()
    
    # Удаление по значению
    print("Удаляем первое вхождение значения 4:")
    lst.remove(4)
    print(f"Список: {lst}")
    print(f"Красивое представление: {str(lst)}")
    print()


def demo_iteration():
    """Демонстрация итерации."""
    print("=" * 50)
    print("ИТЕРАЦИЯ ПО СПИСКУ")
    print("=" * 50)
    
    lst = SinglyLinkedList()
    lst.append("A")
    lst.append("B")
    lst.append("C")
    
    print(f"Список: {lst}")
    print(f"Красивое представление: {str(lst)}")
    print()
    
    print("Итерация через for loop:")
    for i, value in enumerate(lst):
        print(f"  Индекс {i}: {value}")
    print()
    
    print("Преобразование в list:")
    values = list(lst)
    print(f"  {values}")
    print()


def demo_error_handling():
    """Демонстрация обработки ошибок."""
    print("=" * 50)
    print("ОБРАБОТКА ОШИБОК")
    print("=" * 50)
    
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(2)
    
    # Попытка вставки по неверному индексу
    print("Попытка insert(10, 99) в список размера 2:")
    try:
        lst.insert(10, 99)
    except IndexError as e:
        print(f"  Поймано исключение: {e}")
    print()
    
    # Попытка удаления по неверному индексу
    print("Попытка remove_at(10) в список размера 2:")
    try:
        lst.remove_at(10)
    except IndexError as e:
        print(f"  Поймано исключение: {e}")
    print()
    
    # Попытка удаления несуществующего значения
    print("Попытка remove(99) (значение отсутствует):")
    try:
        lst.remove(99)
    except ValueError as e:
        print(f"  Поймано исключение: {e}")
    print()
    
    # Попытка удаления из пустого списка
    empty_lst = SinglyLinkedList()
    print("Попытка remove_at(0) из пустого списка:")
    try:
        empty_lst.remove_at(0)
    except IndexError as e:
        print(f"  Поймано исключение: {e}")


def demo_edge_cases():
    """Демонстрация граничных случаев."""
    print("=" * 50)
    print("ГРАНИЧНЫЕ СЛУЧАИ")
    print("=" * 50)
    
    lst = SinglyLinkedList()
    
    # Вставка в начало и конец пустого списка
    print("Вставка в пустой список:")
    lst.insert(0, "начало")
    print(f"  insert(0, 'начало'): {lst}")
    lst.insert(1, "конец")
    print(f"  insert(1, 'конец'): {lst}")
    print()
    
    # Удаление единственного элемента
    print("Удаление единственного элемента:")
    single = SinglyLinkedList()
    single.append("один")
    print(f"  До удаления: {single}")
    single.remove_at(0)
    print(f"  После remove_at(0): {single}")
    print(f"  Размер: {len(single)}")


def main():
    """Основная функция для запуска демонстраций."""
    demo_basic_operations()
    print()
    demo_removal()
    print()
    demo_iteration()
    print()
    demo_error_handling()
    print()
    demo_edge_cases()


if __name__ == "__main__":
    main()