# python_labs

## Лабораторная 1

### Задание 1

![Картинка 1](./images/lab01/img01.png)


### Задание 2

![Картинка 2](./images/lab01/img02.png)


### Задание 3

![Картинка 3](./images/lab01/img03.png)


### Задание 4

![Картинка 4](./images/lab01/img04.png)


### Задание 5

![Картинка 5](./images/lab01/img05.png)


### Задание 6

![Картинка 6](./images/lab01/img06.png)

### Задание 7

![Картинка 7](./images/lab01/img07.png)



## Лабораторная 2

### Задание 1
#### 1 функция
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError('Список пуст')
    return (min(nums), max(nums))
```
![Картинка 1](./images/lab02/img01.png)
#### 2 функция
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if nums == []:
        return []
    else:
        return sorted(set(nums))
```
![Картинка 2](./images/lab02/img02.png)
#### 3 функция
```python
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for i in mat:
        if not isinstance(i, (tuple, list)):
            raise TypeError('строка не строка строк матрицы')
        result.extend(i)
    return result
```
![Картинка 3](./images/lab02/img03.png)


### Задание B
#### 1 функция
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []:
        return []
    
    n_len = len(mat[0])
    for n in mat:
        if len(n) != n_len:
            raise ValueError('рваная матрица')
    
    return [list(j) for j in zip(*mat)]
```
![Картинка 4](./images/lab02/img04.png)
#### 2 функция
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    n_len = len(mat[0])
    for n in mat:
        if len(n) != n_len:
            raise ValueError('рваная')
    
    result = []
    for i in mat:
        result.append(sum(i))
    return result
```
![Картинка 5](./images/lab02/img05.png)
#### 3 функция
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    n_len = len(mat[0])
    for n in mat:
        if len(n) != n_len:
            raise ValueError('рваная')
    
    result = []
    for i, e in zip(mat[0], mat[1]):
        result.append(i + e)
    return result
```
![Картинка 6](./images/lab02/img06.png)



### Задание С
![Картинка 7](./images/lab02/img07.png)

#### Пример с ошибкой TypeError
гпа вводим не вещественное
![Картинка 8](./images/lab02/img08.png)


## Лабораторная 3
### Задание А
функция normalize
![Картинка 1](./images/lab03/img01.png)
функция tokenize
![Картинка 2](./images/lab03/img02.png)
функция top_n
![Картинка 3](./images/lab03/img03.png)

### Задание В
