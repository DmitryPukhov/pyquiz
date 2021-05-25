import unittest


class Solution:
    """
    227. Basic Calculator II
    Given a string s which represents an expression, evaluate this expression and return its value.
    The integer division should truncate toward zero.
    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
    such as eval().
    Constraints:

    1 <= s.length <= 3 * 105
    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 231 - 1].
    The answer is guaranteed to fit in a 32-bit integer.
    """

    def calculate(self, s: str) -> int:
        # Left operand start pos
        i = 0
        i1 = 0  # Start of operand
        s = s.replace(" ", "")
        stack = []

        while i < len(s):
            # Get digit
            if s[i].isnumeric() or s[i] == ' ':
                i += 1
                continue
            x = int(s[i1:i])
            # Get operation
            rightop = s[i]

            i1 = i + 1  # Index of next operand

            if not stack:
                # Initial block
                stack.append((x, rightop))
                i += 1
                continue

            # Process the stack
            while stack and (stack[-1][1] in {'*', '/'} or rightop in {'+','-'}):
                # If left operation priority is low, push right to the stack
                (leftx,leftop)=stack.pop()
                x = self.calc(leftx,x,leftop)

            stack.append((x,rightop))
            i += 1

        # Calculate what left in stack
        x = int(s[i1:i])

        if not stack:
            return x
        rightx = x
        while stack:
            leftx, leftop = stack.pop()
            rightx = self.calc(leftx, rightx, leftop)
        return rightx

    def calc(self, x1, x2, f):
        out = None
        if f == '+':
            out = x1 + x2
        elif f == '-':
            out = x1 - x2
        elif f == '*':
            out = x1 * x2
        elif f == '/':
            out = x1 // x2
        return out


class BasicCalculatorTest(unittest.TestCase):
    def test_2minus3div4minus1(self):
        self.assertEqual(32, Solution().calculate("1*2-3/4+5*6"))

    def test_example_1mul2minus3div4plus5mul6minus7mul8plus9div10(self):
        self.assertEqual(-24, Solution().calculate("1*2-3/4+5*6-7*8+9/10"))

    def test_example_14div3mul2plus14div4mul3(self):
        self.assertEqual(17, Solution().calculate("14/3*2+15/4*3"))

    def test_example_14div3mul2div4(self):
        self.assertEqual(2, Solution().calculate("14/3*2/4"))

    def test_example_14div3mul2(self):
        self.assertEqual(8, Solution().calculate("14/3*2"))

    def test_example_1plus3plus3(self):
        self.assertEqual(6, Solution().calculate("1+2+3"))

    def test_example_1mul2plus3mul4(self):
        self.assertEqual(14, Solution().calculate("1*2+3*4"))

    def test_example_1plus2mul3plus4mul5(self):
        self.assertEqual(22, Solution().calculate("1+2*3+3*5"))

    def test_example_1plus2mul3plus4mul5plus6(self):
        self.assertEqual(28, Solution().calculate("1+2*3+3*5+6"))

    def test_example_2mul3plus4mul5plu26(self):
        self.assertEqual(27, Solution().calculate("2*3+3*5+6"))

    def test_example1(self):
        """
        Example 1:
        Input: s = "3+2*2"
        Output: 7
        """
        self.assertEqual(7, Solution().calculate("3+2*2"))

    def test_example2(self):
        """
        Example 2:

        Input: s = " 3/2 "
        Output: 1
        """
        self.assertEqual(1, Solution().calculate("3/2"))

    def test_example3(self):
        """
        Example 3:
        Input: s = " 3+5 / 2 "
        Output: 5
        """
        self.assertEqual(5, Solution().calculate("3+5 / 2"))

    def test_example_1(self):
        self.assertEqual(1, Solution().calculate("1"))


if __name__ == '__main__':
    unittest.main()
