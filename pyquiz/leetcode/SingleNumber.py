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
        """
        Check each bit
        mask    b1  mask after b1   b2  mask after b2
        1       1   0               1   1
        1       0   1               0   1
        If mask changed, this bit is even and is present in result number
        """
        mask = 1
        res = 0
        for i in range(0, 64):
            resmask = mask
            for n in nums:
                  resmask = resmask ^ (mask & n)
            if resmask ^ mask:
                res |= mask
            mask <<= 1
        return res
