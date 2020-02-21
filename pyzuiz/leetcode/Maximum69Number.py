class Maxumum69Number:
    """
    Given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



    Example 1:

    Input: num = 9669
    Output: 9969
    Explanation:
    Changing the first digit results in 6669.
    Changing the second digit results in 9969.
    Changing the third digit results in 9699.
    Changing the fourth digit results in 9666.
    The maximum number is 9969.

    Example 2:

    Input: num = 9996
    Output: 9999
    Explanation: Changing the last digit 6 to 9 results in the maximum number.

    Example 3:

    Input: num = 9999
    Output: 9999
    Explanation: It is better not to apply any change.
    """


def maximum_69_number(self, num: int) -> int:
    i = 1
    d = num
    maxi6 = 0
    while d != 0:
        # Get digi
        d = self.digit_of(num, i)
        if d == 6:
            maxi6 = i
        i += 1
    changed = self.with_digit(num, 9, maxi6)
    return changed


@staticmethod
def digit_of(num, i):
    return (num % (10 ** i)) // (10 ** (i - 1))


@staticmethod
def with_digit(n, d, i):
    if i == 0:
        return n

    n1 = n // (10 ** i) * (10 ** i)
    n2 = d * (10 ** (i - 1))
    n3 = n % 10 ** (i - 1)
    return n1 + n2 + n3
