from collections import deque
from typing import List


class RottingOranges:
    """
    In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

    Example 1:
    Input: [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

    Example 2:
    Input: [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

    Example 3:
    Input: [[0,2]]
    Output: 0
    Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

    Note:
    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # DFS approach with queue
        q = deque()
        minutes = 0
        fresh_cnt = 0
        # Rot oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_cnt += 1

        q.append((-1, -1))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            (row, col) = q.popleft()
            if (row, col) == (-1, -1):
                if q:
                    minutes += 1
                    q.append((-1, -1))
                    continue
                else:
                    break
            for dx, dy in directions:
                rownext, colnext = row + dx, col + dy
                if 0 <= rownext < rows and 0 <= colnext < cols:
                    if grid[rownext][colnext] == 1:
                        grid[rownext][colnext] = 2
                        fresh_cnt -= 1
                        q.append((rownext, colnext))

        # Check if all are rotted
        return minutes if not fresh_cnt else -1
