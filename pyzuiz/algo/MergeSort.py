class MergeSort:
    def sort(self, arr: []):
        if len(arr) <= 1:
            return arr
        (arr1, arr2) = self._split(arr)
        return self._merge(self.sort(arr1), self.sort(arr2))

    def _split(self, arr: []):
        """
        Sort given array with merge sort
        :param arr: array to sort
        :return: sorted array
        """

        if len(arr) == 0:
            return [], []

        # Split to arr1 and arr2
        pmiddle = len(arr) // 2
        arr1 = []
        arr2 = []
        for i in range(0, pmiddle):
            arr1.append(arr[i])
        for i in range(pmiddle, len(arr)):
            arr2.append(arr[i])

        return arr1, arr2

    def _merge(self, arr1: [], arr2: []):
        """
        Merge step
        :param arr1: left arr
        :param arr2: right arr
        :return: merged arr
        """
        merged = []
        p1 = p2 = 0
        # Merge arrays
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] < arr2[p2]:
                merged.append(arr1[p1])
                p1 += 1
            else:
                merged.append(arr2[p2])
                p2 += 1
        # Add remainders if exist
        for p1 in range(p1, len(arr1)):
            merged.append(arr1[p1])
            p1 += 1
        for p2 in range(p2, len(arr2)):
            merged.append(arr2[p2])
            p2 += 1
        return merged
