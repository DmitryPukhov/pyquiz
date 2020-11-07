class ZigZagConversion:
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);

    Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

    Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
    """

    def convert(self, s: str, numRows: int) -> str:
        ls = len(s)
        cols = ls // numRows + int(ls % numRows > 0)
        cols *= 2
        # zigzag matrix
        zm = [[None for c in range(cols)] for r in range(numRows)]
        r = 0
        c = 0
        # Fill zigzagmatrix, moving zigzag up-down
        for i in range(ls):
            isodd = c % 2 == 0
            zm[r][c] = s[i]
            if isodd:
                r += 1
                if r == numRows:
                    r, c = (r - 2, c + 1) if r > 2 else (0, c + 2)
            else:
                # Nod odd
                r -= 1
                if r == 0:
                    c += 1
        out = []

        # Go through zigzag matrix row by rowK
        for r in range(numRows):
            for c in range(cols):
                if zm[r][c]: out.append(zm[r][c])
        return ''.join(out)
