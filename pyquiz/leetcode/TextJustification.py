import unittest
from typing import List
from unittest import TestCase


class Solution:
    """
    68. Text Justification
    Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters
    and is fully (left and right) justified.
    You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
    Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
    Extra spaces between words should be distributed as evenly as possible.
    If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned
    more spaces than the slots on the right.
    For the last line of text, it should be left justified and no extra space is inserted between words.

    Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

    Constraints:
    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
    """

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        out = []

        line = []
        linewordslen = 0
        for nextword in words:
            # If whitespaces + words + new word
            if (len(line) - 1) + linewordslen + 1 + len(nextword) <= maxWidth:
                # If still the same line
                line.append(nextword)
                linewordslen += len(nextword)
            else:
                # Add new justified line
                out.append(self.justify_line(line, maxWidth))
                # Reset current line
                line, linewordslen = [nextword], len(nextword)

        # handle last line
        out.append(" ".join(line).ljust(maxWidth, " "))

        return out

    def justify_line(self, line: List[str], width):
        # Calculate space width and number of spaces
        wordswidth = sum([len(w) for w in line])
        spaces = len(line) - 1
        spacewidth = (width - wordswidth) // spaces if spaces else 0

        # Handle extraspaces to fill from left
        extraspaces = width - (wordswidth + spaces * spacewidth) if spaces else 0
        for i in range(extraspaces):
            line[i] += " "

        # Construct justified line
        ws = " " * spacewidth
        return ws.join(line).ljust(width, " ")


class TestJustification(TestCase):
    def test_everything_else_we_do_20(self):
        self.assertEqual(["everything  else  we", "do                  "],
                         Solution().fullJustify(["everything", "else", "we", "do"], 20))

    def test_example1(self):
        """
        Example 1:
        Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
        Output:
        [
           "This    is    an",
           "example  of text",
           "justification.  "
        ]
        """
        res = Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)
        self.assertEqual([
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
            , res)

    def test_example2(self):
        """
        Example 2:

        Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
        Output:
        [
          "What   must   be",
          "acknowledgment  ",
          "shall be        "
        ]
        Explanation: Note that the last line is "shall be    " instead of "shall     be",
        because the last line must be left-justified instead of fully-justified.
        Note that the second line is also left-justified becase it contains only one word.
        """
        res = Solution().fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16)
        self.assertEqual(
            [
                "What   must   be",
                "acknowledgment  ",
                "shall be        "
            ], res)

    def test_example3(self):
        """
        Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
        Output:
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        """
        res = Solution().fullJustify(
            words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a",
                   "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth=20)
        self.assertEqual([
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ], res)
