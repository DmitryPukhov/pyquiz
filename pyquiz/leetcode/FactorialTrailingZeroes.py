class FactorialTrailingZeroes:
    """
    Given an integer n, return the number of trailing zeroes in n!.

    Example 1:
    Input: 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.

    Example 2:
    Input: 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

    Note: Your solution should be in logarithmic time complexity.
    """

    def trailingZeroes(self, n: int) -> int:
        """
        n! = 1*2*...*n
        let's split the digits to prime numbers:
        n!= 1*2*3*(4=2*2)*5*(6=2*3)...
        Each 5 in this sequence adds one trailing zero.
        Calculate fives in this prime numbers sequence multiplication. It is a number of traling zeroes
        """
        y, zeroes = n, 0
        while abs(y) >= 5:
            y = int(y / 5)
            zeroes += y
        return zeroes
