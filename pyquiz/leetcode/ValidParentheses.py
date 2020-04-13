class ValidParentheses:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    Example 1:
    Input: "()"
    Output: true

    Example 2:
    Input: "()[]{}"
    Output: true

    Example 3:
    Input: "(]"
    Output: false

    Example 4:
    Input: "([)]"
    Output: false

    Example 5:
    Input: "{[]}"
    Output: true
    """
    pairs = dict({'(': ')', '{': '}', '[': ']'})

    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if self.is_open(c):
                stack.append(c)
                continue
            else:
                prev = stack.pop() if stack else None
                if not self.is_pair(prev, c):
                    return False
        return not stack

    def is_pair(self, b1, b2):
        if b1 is None or b2 is None:
            return False
        return b2 == self.pairs[b1]

    def is_open(self, c):
        return c in self.pairs.keys()
