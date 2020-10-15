from array import array
from typing import List


class MaximalSquare:
    """
    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

    Example:
    Input:
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    Output: 4
    """

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        rows = len(matrix)

        for row in range(0, rows):
            for col in range(0, cols):
                matrix[row][col] = int(matrix[row][col])
        # Sums in rows or cols
        for row in range(1, rows):
            for col in range(1, cols):
                if not matrix[row][col]:
                    continue
                matrix[row][col] = min([matrix[row - 1][col] + 1,
                                        matrix[row][col - 1]+1,
                                        matrix[row-1][col-1]+1])

        side=max([max(r) for r in matrix])
        return side * side
