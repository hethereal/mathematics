"""
实现一个矩阵到简化阶梯形的算法
"""
from fractions import Fraction

A = [[0, 3, -6, 6, 4, -5],
     [3, -7, 8, -5, 8, 9],
     [3, -9, 12, -9, 6, 15]]

def solve(arr: list):
    """
    矩阵到简化阶梯形
    :param arr: 矩阵
    :return: 简化阶梯型
    """
    if not arr:
        return []

    matrix = [[Fraction(value) for value in row] for row in arr]
    rows, cols = len(matrix), len(matrix[0])
    pivot_row = 0

    for col in range(cols):
        if pivot_row == rows:
            break
        selected = next(
            (row for row in range(pivot_row, rows) if matrix[row][col] != 0),
            None
        )
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        pivot = matrix[pivot_row][col]
        matrix[pivot_row] = [value / pivot for value in matrix[pivot_row]]

        # 把主元上方和下方的元素都消成 0
        for row in range(rows):
            if row == pivot_row:
                continue

            factor = matrix[row][col]
            if factor != 0:
                matrix[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(matrix[row], matrix[pivot_row])
                ]

        pivot_row += 1

    return matrix

if __name__ == '__main__':
    result = solve(A)
    print(result)


