class BasicCalculator:
    """
    Implement a basic calculator to evaluate a simple expression string.
    The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
    non-negative integers and empty spaces .

    Example 1:
    Input: "1 + 1"
    Output: 2

    Example 2:
    Input: " 2-1 + 2 "
    Output: 3

    Example 3:
    Input: "(1+(4+5+2)-3)+(6+8)"
    Output: 23

    Note:
    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
    """

    def calculate(self, s: str) -> int:
        #s = s.replace(" ", "")
        opstack = []
        token = []
        op = None

        for i, c in enumerate(s):
            if c == " ":
                continue
            if c == '(':
                opstack.append((0, '+'))
                if token and op:
                    opstack.append((int(''.join(token)), op))
                    token, op = [], None
                continue
            elif c == ')':
                (left, op) = opstack.pop() if opstack else (0, '+')
                right = int(''.join(token)) if token else 0
                res = self.calc(left, op, right)
                token = list(str(res))
            elif c.isnumeric():
                # Number
                token.append(c)
            else:
                # Operation sign
                if opstack and token:
                    #!!! here 3-(1-2)
                    # In 2 + 3 - 1 we reached - and have 2+ in stack and 3 in token
                    (left, op) = opstack.pop()
                    right = int(''.join(token))
                    left = self.calc(left, op, right)
                    opstack.append((left, c))
                    token, op = [], None
                elif opstack:
                    (stacktoken, _) = opstack.pop()
                    opstack.append((stacktoken, c))
                elif token:
                    # In 2 + 3 - 1 we reached + and have 2 in token
                    opstack.append((int(''.join(token)), c))
                    token, op = [], None
                else:
                    opstack.append((0, c))

        # Calculate output from last token and stack
        out = int(''.join(token)) if token else 0
        while opstack:
            (left, op) = opstack.pop()
            out = self.calc(left, op, out)
        return out

    def calc(self, left: int, op: str, right: int):
        if op == '+':
            return left + right
        else:
            return left - right
