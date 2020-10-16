from typing import List


class SpiralMatrix:
    """
    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

    Example 1:
    Input:
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:
    Input:
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m1, m2 = 0, len(matrix)
        n1, n2 = 0, len(matrix[0])
        out = []
        while m1 < m2 and n1 < n2:
            # top
            for n in range(n1, n2):
                out.append(matrix[m1][n])
            # right
            for m in range(m1 + 1, m2):
                out.append(matrix[m][n2 - 1])
            # bottom
            if m2 - 1 > m1:
                for n in range(n2 - 2, n1 - 1, -1):
                    out.append(matrix[m2 - 1][n])
            # left
            if n1 < n2 - 1:
                for m in range(m2 - 2, m1, -1):
                    out.append(matrix[m][n1])
            n1 += 1
            n2 -= 1
            m1 += 1
            m2 -= 1
        return out
