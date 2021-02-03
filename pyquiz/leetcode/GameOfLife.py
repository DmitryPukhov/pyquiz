from collections import defaultdict
from typing import List


class Solution:
    """
    289. Game of Life
    According to Wikipedia's article: "The Game of Life, also known simply as Life,
    is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    The board is made up of an m x n grid of cells, where each cell has an initial state:
    live (represented by a 1) or dead (represented by a 0).
    Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
    using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    The next state is created by applying the above rules simultaneously to every cell in the current state,
    where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

    Example 1:
    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    Example 2:
    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]

    Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is 0 or 1.

    Follow up:

    Could you solve it in-place? Remember that the board needs to be updated simultaneously:
    You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite,
    which would cause problems when the active area encroaches upon the border of the array (i.e.,
    live cells reach the border). How would you address these problems?
    """

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        nx = len(board[0])
        ny = len(board)
        # Fill in (x,y)->neighbors
        # neighbors = defaultdict(int)
        for x in range(0, nx):
            for y in range(0, ny):
                dxdy = [(1, 0), (1, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, -1), (0, 1)]
                for (dx, dy) in dxdy:
                    if (0 <= (x + dx) < nx) and (0 <= (y + dy) < ny) and board[y + dy][x + dx] % 10:
                        board[y][x] += 10
                        # neighbors[(x, y)] += 1

        # Update the board
        for x in range(0, nx):
            for y in range(0, ny):
                cell = board[y][x] % 10
                neighbors = board[y][x] // 10
                board[y][x] = 0
                # if board[y][x] %  and neighbors[(x, y)] < 2:
                if cell and neighbors < 2:
                    # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                    # board[y][x] =0
                    board[y][x] = 0
                elif cell and 2 <= neighbors <= 3:
                    # Any live cell with two or three live neighbors lives on to the next generation.
                    # board[y][x] = 1
                    board[y][x] = 1
                elif cell and neighbors > 3:
                    # Any live cell with more than three live neighbors dies, as if by over-population.
                    # board[y][x] = 0
                    board[y][x] = 0
                elif not cell and neighbors == 3:
                    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    # board[y][x] = 1
                    board[y][x] = 1

        # for x in range(0, nx):
        #     for y in range(0, ny):
        #         cell = board[y][x]
        #         board[y][x] = (2 & (cell % 10)) >> 1
