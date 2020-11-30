# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class LeftmostColumnWithAtLeastAOne:
    """
    (This problem is an interactive problem.)
    A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

    Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
    You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

    BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
    BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
    Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

    For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

    Example 1:
    Input: mat = [[0,0],[1,1]]
    Output: 0

    Example 2:
    Input: mat = [[0,0],[0,1]]
    Output: 1

    Example 3:
    Input: mat = [[0,0],[0,0]]
    Output: -1

    Example 4:
    Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
    Output: 1

    Constraints:
    rows == mat.length
    cols == mat[i].length
    1 <= rows, cols <= 100
    mat[i][j] is either 0 or 1.
    mat[i] is sorted in a non-decreasing way.
    """

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        (height, width) = binaryMatrix.dimensions()
        l, r = 0, width - 1
        rows = range(0, height)
        out = -1
        while l < r:
            p = min(width, l + (r - l) // 2)
            newrows=[]
            for row in rows:
                if (binaryMatrix.get(row, p)):
                    newrows.append(row)
            if newrows:
                # Got 1, move left
                r = max(0, p - 1)
                rows = newrows
                out = p
            else:
                # Didn't get 1, move right
                l = min(width - 1, p + 1)

        for row in rows:
            if (binaryMatrix.get(row, l)):
                return l
        return out
