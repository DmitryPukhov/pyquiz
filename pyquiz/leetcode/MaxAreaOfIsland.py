from typing import List


class MaxAreaOfIsland:
    """
    Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
    connected 4-directionally (horizontal or vertical.)
    You may assume all four edges of the grid are surrounded by water.
    Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

    Example 1:

    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

    Example 2:

    [[0,0,0,0,0,0,0,0]]
    Given the above grid, return 0.

    Note: The length of each dimension in the given grid does not exceed 50.
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.visited = set()
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        out = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                out = max(out, self.get_area(row, col))
        return out

    def get_area(self, row, col):
        """
        Recursively get aread of island
        """
        if row >= self.rows or row < 0 or col >= self.cols or col < 0:
            return 0
        if (row, col) in self.visited:
            return 0
        if self.grid[row][col] == 0:
            return 0
        self.visited.add((row, col))
        area = 1
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for d in deltas:
            area += self.get_area(row + d[0], col + d[1])

        return area
