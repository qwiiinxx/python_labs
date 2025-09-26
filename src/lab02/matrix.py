def transpose(nums):
    if nums == []:
        return []
    
    n_len = len(nums[0])
    for n in nums:
        if len(n) != n_len:
            raise ValueError('рваная матрица')
    
    return [list(j) for j in zip(*nums)]

# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))

def row_sums(nums):
    n_len = len(nums[0])
    for n in nums:
        if len(n) != n_len:
            raise ValueError('рваная')
    
    result = []
    for i in range(len(nums)-1):
        if len(nums[i]) == 3:
            sum1 = nums[i][0] + nums[i][1] + nums[i][2]
            result.append(sum1)
            sum2 = nums[i+1][0] + nums[i+1][1] + nums[i+1][2]
            result.append(sum2)
        else:
            sum1 = nums[i][0] + nums[i][1]
            result.append(sum1)
            sum2 = nums[i+1][0] + nums[i+1][1]
            result.append(sum2)

    return result

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

def col_sums(nums):
    n_len = len(nums[0])
    for n in nums:
        if len(n) != n_len:
            raise ValueError('рваная')
    
    result = []
    for i in range(len(nums)-1): # [[1, 2, 3], [4, 5, 6]] -> [5, 7, 9]
        if len(nums[i]) == 3:
            sum1 = nums[i][0] + nums[i+1][0]
            result.append(sum1)
            sum2 = nums[i][1] + nums[i+1][1]
            result.append(sum2)
            sum3 = nums[i][2] + nums[i+1][2]
            result.append(sum3)
        else:                                # [[-1, 1], [10, -10]] -> [9, -9]
            sum1 = nums[i][0] + nums[i+1][0]
            result.append(sum1)
            sum2 = nums[i][1] + nums[i+1][1]
            result.append(sum2)

    return result

print(col_sums([[1, 2, 3], [4, 5, 6]])) # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]])) # [9, -9]
print(col_sums([[0, 0], [0, 0]])) # [0, 0]
print(col_sums([[1, 2], [3]]))