class ReverseInteger(object):
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
    Input: 123
    Output: 321

    Example 2:
    Input: -123
    Output: -321

    Example 3:
    Input: 120
    Output: 21
    """

    def reverse(self, x):
        is_neg = x < 0
        x = abs(x)
        # Store digits in array
        digits = []
        i = 0
        d = -1
        while x >= 10 ** i:
            d = self.digit(x, i)
            digits.append(d)
            i += 1
        # Restore digits in reverse order
        res = 0
        j = i - 1
        for d in digits:
            res += d * 10 ** j
            j -= 1
        if is_neg:
            res = - res

        return res if -2 ** 31 < res < 2 ** 31 - 1 else 0

    def digit(self, x, i):
        """
        :param x: number
        :param i: zero-based index of digit from the right
        :return:  digit
        """
        return x % 10 ** (i + 1) // 10 ** i

    @staticmethod
    def reverse_by_string(x):
        """
        Converts int to string, reverse string, returns new int
        """
        rev_string = str(x)[::-1]
        if rev_string.endswith('-'):
            rev_string = '-' + rev_string.rstrip('-')
        return int(rev_string)
