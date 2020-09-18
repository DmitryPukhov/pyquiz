from typing import List


class ContainerWithMostWater:
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.
    """

    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = (0, len(height) - 1)
        out = (r - l) * min(height[l], height[r])
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            out = max(out,(r - l) * min(height[l], height[r]))
        return out
