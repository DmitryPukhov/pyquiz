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
        magic_index = []

        for i in range(0, len(arr)):
            a = arr[i]
            if a == i:
                # Found magic index
                magic_index.append(a)
            elif magic_index:
                # End of magic index, return it
                return magic_index
            # No magic index, continue search

        return magic_index

