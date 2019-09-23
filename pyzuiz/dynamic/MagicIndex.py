import math


class MagicIndex:
    """
    8.3
    Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
    i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
    array A.
    FOLLOW UP
    What if the values are not distinct?
    Hints:#770, #204, #240, #286, #340
    """

    def single(self, arr: []):
        """
        If the values are distinct, array can contain the only magic index
        O(log(n)) implementation
        :return: (start, end) of magic index
         """
        # Find an element inside magic index
        inside_index = self._any_inside(arr)
        if inside_index is None:
            return None
        start = self._start(arr, inside_index)
        end = self._end(arr, inside_index)
        return start, end

    @staticmethod
    def _start(arr, inside_index):
        """

        :param arr: given array
        :param inside_index: index of element in array, which is inside magic index
        :return: start of magic index
        """
        start = 0
        end = inside_index
        # Repeat until we narrow our search to lower bound
        while start < end:
            if arr[start] == start:
                # We are inside index, move left
                end = start
                start = 0
            else:
                # We are before index, move right
                start = start + math.ceil((end - start) / 2)
        return start

    @staticmethod
    def _end(arr, inside_index):
        """
        :param arr: given array
        :param inside_index: index of element in array, which is inside magic index
        :return: end of magic index
        """
        max_end = len(arr) - 1
        end = max_end
        start = inside_index
        # Repeat until we narrow our search to upper bound
        while start < end:
            if arr[end] == end:
                # We are inside magic index, move right
                start = end
                end = max_end
            else:
                # We are after magic index, move left
                end = start + math.floor((end - start) / 2)
        return end

    @staticmethod
    def _any_inside(arr):
        """
        Find any index inside magic index
        """
        # Using binary division, find start of magic index
        start = 0
        end = len(arr)
        # Find the element inside magic index
        while start < end:
            pivot = int(start + (end - start) / 2)
            if arr[pivot] > pivot:
                # We are on the right of magic index, move left
                end = pivot
            elif arr[pivot] < pivot:
                # We are on the left of magic index, move right
                start = pivot
            else:
                # We are inside magic index
                return pivot
        # Not found
        return None

    @staticmethod
    def multi(arr: []):
        """
        O(n) implementation
        If the values are not distinct, array can contain multiple magic indexes.
        :return: array of tuples[(start1,end1),(start2,end2,)...]
        """
        magic_indexes = []
        # Current magic index start and end
        mi_start = None
        mi_end = None
        # Go through, looking for magic indexes
        for i in range(0, len(arr)):
            a = arr[i]
            if a == i:
                if mi_start is None:
                    # Found start of new magic index
                    mi_start = a
                else:
                    # Update the end of current magic index
                    mi_end = a
            elif mi_start is not None:
                # Next element after magic index. Add magic index to result and reset.
                magic_indexes.append((mi_start, mi_end))
                mi_start = mi_end = None
            # No magic index, continue search

        if mi_start is not None:
            if mi_end is None:
                mi_end = mi_start
            magic_indexes.append((mi_start, mi_end))

        return magic_indexes
