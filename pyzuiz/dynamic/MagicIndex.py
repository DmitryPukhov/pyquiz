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

    @staticmethod
    def of(arr):
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
