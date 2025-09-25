def min_max(nums): # [3, -1, 5, 5, 0]
    if not nums:
        raise ValueError('Список пуст')
    return (min(nums), max(nums))


# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))                 
# print(min_max([-5, -2, -9]))         
# print(min_max([]))                 
# print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums):
    if nums == []:
        return []
    else:
        return sorted(set(nums))
    
# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


def flatten(nums):
    result = []
    for i in nums:
        if not isinstance(i, (tuple, list)):
            raise TypeError('строка не строка строк матрицы')
        result.extend(i)
    return result
    
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))