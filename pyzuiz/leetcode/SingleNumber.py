from typing import List


class SingleNumber:
    """
    Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:
    Input: [2,2,1]
    Output: 1

    Example 2:
    Input: [4,1,2,1,2]
    Output: 4`
    """

    def solve(self, nums: List[int]) -> int:
        resmask = 0
        even_found = False
        for bn in range(0, 32):
            mask = 1 << bn
            bc = 0
            for x in nums:
                if x & mask == mask:
                    bc += 1
            if bc % 2 == 1:
                resmask |= mask
                even_found = True

        if not even_found:
            return 0
        for x in nums:
            if x & resmask == resmask:
                return x
