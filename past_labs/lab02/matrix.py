def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []:
        return []

    n_len = len(mat[0])
    for n in mat:
        if len(n) != n_len:
            raise ValueError("рваная матрица")

    return [list(j) for j in zip(*mat)]


# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    n_len = len(mat[0])
    for n in mat:
        if len(n) != n_len:
            raise ValueError("рваная")

    result = []
    for i in mat:
        result.append(sum(i))
    return result


# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2, 4, 9, 4, 6], [3, 3, 5, 7, 5, 6]]))
# print(row_sums([[1, 2], [3]]))


def col_sums(mat: list[list[float | int]]) -> list[float]:
    n_len = len(mat[0])
    for n in mat:
        if len(n) != n_len:
            raise ValueError("рваная")

    result = []
    for i in range(n_len):
        col_sum = 0
        for j in range(len(mat)):
            col_sum += mat[j][i]
        result.append(col_sum)
    return result


print(col_sums([[1, 2, 3], [4, 5, 6]]))  # [5, 7, 9]
print(col_sums([[1, 3, 3], [1, 1, 1], [1, 1, 1]]))
print(col_sums([[-1, 1], [10, -10]]))  # [9, -9]
print(col_sums([[0, 0], [0, 0]]))  # [0, 0]
print(col_sums([[1, 2], [3]]))
