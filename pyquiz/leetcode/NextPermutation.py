from typing import List


class NextPermutation:
    """
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
    The replacement must be in-place and use only constant extra memory.
    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    """

    def nextPermutation(self, nums: List[int]) -> None:
        if not nums or len(nums) == 1: return
        # Find first decreasing
        # Find next just larger than decreasing
        # Swap
        # sort the right
        i = len(nums) - 2
        while i >= 0:
            # Find first decreasing
            if nums[i] < nums[i + 1]: break
            i -= 1
        if i == -1:
            # If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
            nums.sort()
            return
        # Find next larger than decreasing and swap
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break

        # sort the right
        nums[i + 1:] = sorted(nums[i + 1:])