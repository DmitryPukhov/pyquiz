from typing import List
from heapq import *


class Solution:
    """
    Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

    Example 1:
    Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    Output: 4
    Explanation: After the rain, water is trapped between the blocks.
    We have two small pounds 1 and 3 units trapped.
    The total volume of water trapped is 4.

    Example 2:
    Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    Output: 10

    Constraints:
    m == heightMap.length
    n == heightMap[i].length
    1 <= m, n <= 200
    0 <= heightMap[i][j] <= 2 * 104
    """

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) == 0:
            return 0
        # Init visited set with surroundings
        top = [(heightMap[0][i], 0, i) for i in range(0, len(heightMap[0]))]
        bottom = [(heightMap[len(heightMap) - 1][i], len(heightMap) - 1, i) for i in \
                  range(0, len(heightMap[len(heightMap) - 1]))]
        left = [(heightMap[i][0] if heightMap[i] else 0, i, 0) for i in range(len(heightMap))]
        right = [(heightMap[i][len(heightMap[i]) - 1] if heightMap[i] else 0, i, len(heightMap[i]) - 1) \
                 for i in range(len(heightMap))]
        visited = set(top + bottom + left + right)
        # Init heap with surroundings
        heap = list(visited)
        heapify(heap)

        max_ = float('-inf')
        water = 0
        while heap:
            # Gen min item from heap and put to visited
            value, irow, icol = heappop(heap)
            max_ = max(max_, value)

            # Add to visited and visit neighbors
            visited.add((value, irow, icol))

            # Add neighbors to visited
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= irow + dr < len(heightMap) and 0 <= icol + dc < len(heightMap[irow]):
                    neighbour = (heightMap[irow + dr][icol + dc], irow + dr, icol + dc)
                    if neighbour in visited:
                        continue
                    water += max(0, max_ - neighbour[0])
                    visited.add(neighbour)
                    heappush(heap, neighbour)

        return water
