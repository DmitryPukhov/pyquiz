class SqrtX:
    """
    Implement int sqrt(int x).
    Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
    Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

    Example 1:
    Input: 4
    Output: 2
    Example 2:

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since
    the decimal part is truncated, 2 is returned.
    """

    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        # n1, n2 - bounds for binary search sqrt(x)
        n1 = 0
        n2 = x
        n = x
        is_end = False
        delta = x
        while not is_end:
            n = n1 + (n2 - n1) // 2
            nn = n * n
            if nn > x:
                # n is too high for sqrt
                n2 = n
            else:
                # n is too low or ok for sqrt
                cur_delta = x - nn
                # If our integer is the closest to sqrt
                is_end = cur_delta >= delta
                delta = cur_delta
                n1 = n
        return n
