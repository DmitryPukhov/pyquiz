from collections import defaultdict, deque


class MinimumKnightMoves:
    """
    In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

    A knight has 8 possible moves it can make, as illustrated below.
    Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
    Return the minimum number of steps needed to move the knight to the square [x, y].
    It is guaranteed the answer exists.

    Example 1:
    Input: x = 2, y = 1
    Output: 1
    Explanation: [0, 0] → [2, 1]

    Example 2:
    Input: x = 5, y = 5
    Output: 4
    Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

    Constraints:
    |x| + |y| <= 300
    """

    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([(0, 0, 0)])
        visited = set()
        xx = yy = step = 0
        deltas = [(2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (-1, 2)]
        # Line formula y=ax+b
        while xx != x or yy != y:
            xx, yy, step = q.popleft()
            for (dx, dy) in deltas:
                # If we are at the same quarter or near
                if (xx + dx, yy + dy) in visited:
                    continue
                visited.add((xx + dx, yy + dy))
                q.append((xx + dx, yy + dy, step + 1))

        return step
