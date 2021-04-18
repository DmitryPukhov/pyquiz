from typing import List


class Solution:
    """
    42. Trapping Rain Water
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.

    Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

    Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

    Constraints:
    n == height.length
    0 <= n <= 3 * 104
    0 <= height[i] <= 105
    """

    def trap(self, height: List[int]) -> int:
        return self.trap_2pointers(height)

    def trap_2pointers(self, height: List[int]) -> int:
        if not height:
            return 0
        rightbound = right = len(height) - 1
        leftbound = left = 0

        out = 0
        while left < right:
            if height[left] < height[right]:
                # Move left bound or get water
                if height[left] >= height[leftbound]:
                    # Move right bound
                    leftbound = left
                else:
                    # collect water
                    out += height[leftbound] - height[left]
                left += 1
            else:
                # Move right bound or get water
                if height[right] >= height[rightbound]:
                    # Move left bound
                    rightbound = right
                else:
                    # collect water
                    out +=height[rightbound] - height[right]
                right -= 1

        return out

    def trap_stack(self, height: List[int]) -> int:
        """
        Stack approach: store left bound in a stack
        """
        if not height:
            return 0
        stack = []
        out = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                ibottom = stack.pop()
                if not stack:
                    break
                dist = i - stack[-1] - 1
                volume = (min(height[stack[-1]], h) - height[ibottom]) * dist
                out += volume
            stack.append(i)
        return out

    def trap_dp(self, height: List[int]) -> int:
        """
        The same as bruite force but store left and right bounds in a map: memoisation.
        O(n) runtime, O(n) memory
        """
        if not height:
            return 0
        out = 0

        # Fill in lmax
        lmax = [0] * len(height)
        lmax[0] = height[0]
        for i in range(1, len(height)):
            lmax[i] = max(height[i], lmax[i - 1])

        # Fill in rmax
        rmax = [0] * len(height)
        rmax[-1] = height[-1]
        for i in range(0, len(height) - 1)[::-1]:
            rmax[i] = max(height[i], rmax[i + 1])

        # Go through h, add each bar to out water volume
        for i in range(0, len(height)):
            # Add current bar to out
            curwater = max(0, min(lmax[i], rmax[i]) - height[i])
            out += curwater
        return out

    def trap_bruitforce(self, height: List[int]) -> int:
        """
        Go through array find left bound for each item, fill in left heights array
        Go back and find right bound, fill in right heights array
        Go through again and get water barfor each item bar, considering left and right bounds stored.
        Bad: O(n^2) runtime, O(n) memory
        """
        out = 0
        for i, h in enumerate(height):
            # Find left bound
            lh = max([0] + height[0:i])
            # Find right bound
            rh = max([0] + height[i + 1:])
            # Add current bar to out
            out += max(0, min(lh, rh) - h)
        return out
