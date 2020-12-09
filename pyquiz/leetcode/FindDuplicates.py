from typing import List


class FindDuplicates:
    """
    Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
    Find all the elements that appear twice in this array.
    Could you do it without extra space and in O(n) runtime?

    Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [2,3]
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        numset = set()
        out = []
        while nums:
            # move the last element from input array to the set or out
            n = nums.pop()
            if n in numset:
                numset.remove(n)
                out.append(n)
            else:
                numset.add(n)
        return out
