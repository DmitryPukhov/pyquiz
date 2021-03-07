from functools import lru_cache


class Solution:
    """
    A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

    Given a starting point (sx, sy) and a target point (tx, ty),
    return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty).
    Otherwise, return False.

    Examples:

    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: True
    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)

    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: False

    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: True

    Note:
    sx, sy, tx, ty will all be integers in the range [1, 10^9].
    """

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        x, y = tx, ty
        while x >= sx and y >= sy:
            if x == sx and y == sy:
                break
            if x > y:
                if  y > sy:
                    x %=y
                else:
                    return (x-sx)%y == 0
            else:
                if x > sx:
                    y %= x
                else:
                    return (y-sy)%x == 0

        return x == sx and y == sy

    def reachingPoints_recursive(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        @lru_cache(None)
        def steps(x, y):
            if x == tx and y == ty:
                # We are at the target
                return 0
            elif x > tx or y > ty:
                # We jumped out
                return float('inf')
            stepsx = 1 + steps(x + y, y)
            stepsy = 1 + steps(x, y + x)
            return min(stepsx, stepsy)

        return steps(sx, sy) < float('inf')
