from typing import List


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
                p3 -= 1
            elif nums2[p2] > nums1[p1]:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1
            elif nums1[p1] == nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
                p3 -= 1
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1
        while p1 >= 0:
            nums1[p3] = nums1[p1]
            p1 -= 1
            p3 -= 1

    def print(self, nums1, m, nums2, n):
        print(f'nums1={nums1}, m={m}, \nnums2={nums2}, n={n}')
        self.merge(nums1, m, nums2, n)
        print(f'merged: {nums1}\n')


alg = MergeSortedArray()

alg.print([0, 0, 3, 0, 0, 0, 0, 0, 0], 3, [-1, 1, 1, 1, 2, 3], 6)
# 6
# real: [0, -1, 0, 0, 1, 1, 1, 2, 3]
# expected:[-1,0,0,1,1,1,2,3,3]

alg.print([1, 0], 1, [-1], 1)
alg.print([-1, -1, 0, 0], 2, [-2, -2], 2)
alg.print([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
