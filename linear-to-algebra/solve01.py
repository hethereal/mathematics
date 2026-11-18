"""
实现一个矩阵到简化阶梯形的算法
"""

A = [[0, 3, -6, 6, 4, -5], [3, -7, 8, -5, 8, 9], [3, -9, 12, -9, 6, 15]]

def solve(arr: list):
    """
    矩阵到简化阶梯形
    :param arr: 矩阵
    :return: 简化阶梯型
    """
    # 收集一下各列的数据
    col_arr = []
    for row_arr in A:
        print(col_arr)

if __name__ == '__main__':
    solve(A)


