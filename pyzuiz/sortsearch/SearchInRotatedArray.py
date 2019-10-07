class SearchInRotatedArray:
    """
    10.3
    Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
    number of times, write code to find an element in the array. You may assume that the array was
    originally sorted in increasing order.
    EXAMPLE
    lnput:findSin{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
    Output: 8 (the index of 5 in the array)
    """

    @staticmethod
    def search(x, arr: []):
        """
        Solution: modified binary search.
        Rotated array contains of 2 sorted parts for any number of rotations.
        Split array into 2 chunks. One chunk is sorted (low < high), another is not.
        :param x: element to find index of
        :param arr: rotated array
        :return: index of given element in array
        """

        n = len(arr)

        # Chunk with data: Low, high, pivot
        low = 0
        high = n - 1
        pivot = low + high // 2

        while arr[pivot] != x and high - low > 1:
            pivot = low + (high - low) // 2

            # Check left part
            if arr[low] <= x <= arr[pivot]:
                # Go to left part
                high = pivot
            else:
                # Go to right part
                low = pivot

        # Check whether we have found something good
        if arr[pivot] == x:
            return pivot
        elif arr[low] == x:
            return low
        elif arr[high] == x:
            return high
        return None
