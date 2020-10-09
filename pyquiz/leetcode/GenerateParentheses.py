from typing import List


class GenerateParentheses:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]
    """

    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        self.generate("", n, 0, 0, out)
        return out

    def generate(self, s: str, n: int, leftn: int, rightn: int, out: []):
        if len(s) == n * 2:
            out.append(s)
            return
        if leftn < n:
            self.generate(s + '(', n, leftn + 1, rightn, out)
        if n >= leftn > rightn and rightn < n:
            self.generate(s + ')', n, leftn, rightn + 1, out)
