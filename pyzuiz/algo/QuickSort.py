class QuickSort:
    def sort(self, arr: [], start=None, end=None, pivot=None):

        if start is None:
            start = 0
        if end is None:
            end = len(arr)
        if pivot is None:
            pivot = self._pivot(start, end)
        if end - start <= 0:
            return []
        elif end - start == 1:
            return [arr[start]]

        # Partition around pivot
        pivot = self._partition(arr, start, pivot, end)

        # Recursive call for left/right partitions
        return self.sort(arr, start, pivot) + self.sort(arr, pivot, end)

    def _partition(self, arr, start, pivot, end):
        # Go and do p1 swap p2 if needed
        p1 = start
        p2 = end - 1
        while p1 < pivot and p2 > pivot:
            # Go until arr[p1]> pivot and arr[p2] < pivot
            while arr[p1] < arr[pivot] and p1 < pivot:
                p1 += 1
            while arr[p2] > arr[pivot] and p2 > pivot:
                p2 -= 1
            # Swap
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1

        # If arr[p2] is smaller than arrp[pivot], move arr[p2] before pivot
        while p2 > pivot:
            if arr[p2] < arr[pivot]:
                arr[pivot], arr[p2] = arr[p2], arr[pivot]
                pivot += 1
            p2 -= 1
        # If arr[p1] is larger than arr[pivot], move arr[p1] after pivot
        while p1 < pivot:
            if arr[p1] > arr[pivot]:
                arr[pivot], arr[p1] = arr[p1], arr[pivot]
                pivot -= 1
            p1 += 1
        return self._pivot(start, end)

    def _pivot(self, start, end):
        """
        Calculate pivot index
        :param start: start index
        :param end: end index
        :return:
        """
        return start + (end - start) // 2
