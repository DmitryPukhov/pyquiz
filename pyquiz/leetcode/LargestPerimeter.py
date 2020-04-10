from typing import List


class LargestPerimeter:
    """
    Given an array A of positive lengths, return the largest
    perimeter of a triangle with non-zero area, formed from 3 of these lengths.
    If it is impossible to form any triangle of non-zero area, return 0.
    """

    def largestPerimeter(self, A: List[int]) -> int:
        # Get largest lengths
        A.sort(reverse=True)
        # Get first 3 largest lengths which can form triangle
        for i in range(0, len(A) - 3 + 1):
            if A[i] + A[i + 1] > A[i + 2] and A[i + 1] + A[i + 2] > A[i] and A[i] + A[i + 2] > A[i + 1]:
                return sum(A[i:i + 3])

        return 0


print(LargestPerimeter().largestPerimeter([2, 1, 2, 3]))
