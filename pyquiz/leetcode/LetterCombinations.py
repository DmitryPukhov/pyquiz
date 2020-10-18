from typing import List


class LetterCombinations:
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations
    that the number could represent. Return the answer in any order.
    A mapping of digit to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letter

    Mapping

    Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Example 2:
    Input: digits = ""
    Output: []

    Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

    Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9']
    """
    _m = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            # Last digit, no right part
            return self._m[digits[0]]
        out = []
        for l in self._m[digits[0]]:
            # Recursively get right part after first digit
            rights = self.letterCombinations(digits[1:])
            # First digit concat right part are all combinations
            out.extend([l+right for right in rights])
        return out

