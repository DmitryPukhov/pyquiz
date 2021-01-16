from typing import List


class MaximalRectangle:
    """
    Given a rows x cols binary matrix filled with 0's and 1's,
    find the largest rectangle containing only 1's and return its area.

    Example 1:
    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 6
    Explanation: The maximal rectangle is shown in the above picture.

    Example 2:
    Input: matrix = []
    Output: 0

    Example 3:
    Input: matrix = [["0"]]
    Output: 0

    Example 4:
    Input: matrix = [["1"]]
    Output: 1

    Example 5:
    Input: matrix = [["0","0"]]
    Output: 0

    Constraints:
    rows == matrix.length
    cols == matrix.length
    0 <= row, cols <= 200
    matrix[i][j] is '0' or '1'.
    """

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Go through matrix and track left, right points and height of rectangle for this point
        """
        if not matrix:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])

        h = [0] * ncols
        l = [0] * ncols
        r = [ncols] * ncols
        out = 0
        for i in range(0, nrows):

            curl = 0
            # Fill in left bound for each row
            for j in range(0, ncols):
                if matrix[i][j] == '1':
                    l[j] = max(l[j], curl)
                    h[j] += 1
                else:
                    h[j] = 0
                    l[j] = 0
                    curl = j+1
            # Fill in right bound for each row
            curr = ncols
            for j in range(ncols - 1, -1, -1):
                if matrix[i][j] == '1':
                    r[j] = min(r[j], curr)
                else:
                    r[j] = ncols
                    curr = j

            # Calc  max area found up to this row
            for j in range(0, ncols):
                out = max(out, h[j] * (r[j] - l[j]))

        return out
