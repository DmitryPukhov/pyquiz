from typing import List


class SelfDividingNumbers:
    """
     A self-dividing number is a number that is divisible by every digit it contains.
    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
     Also, a self-dividing number is not allowed to contain the digit zero.
     Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

     Example 1:
     Input:
     left = 1, right = 22
     Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
     Note:
     The boundaries of each input argument are 1 <= left <= right <= 10000.
     """

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = list()
        for x in range(left, right + 1):
            if self.is_self_div(x):
                res.append(x)

        return res

    def is_self_div(self, x):
        # Get max digit pos from right
        maxp = 0
        while 10 ** maxp < x:
            maxp += 1

        # Check each digit in x
        for p in range(0, maxp):
            digit = x % 10 ** (p + 1) // 10 ** p
            if digit == 0 or x % digit != 0:
                return False
        return True
