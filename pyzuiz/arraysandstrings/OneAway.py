import math


class OneAway:
    """
    One Away: There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check if they are
    one edit (or zero edits) away.
    EXAMPLE
    ->
    pales, ple -> true
    pales, pale -> true
    pale, bake -> false
    """

    @staticmethod
    def is_one_away(s1: str, s2: str):
        # Will be set to true after first edit of any string
        is_edited = False
        # Move pointers along strings
        p1 = 0
        p2 = 0

        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
                continue

            if is_edited:
                # chars not equal but we already did one edit
                return False

            if p1 + 1 == len(s1) and p2 + 1 == len(s2):
                return True
            elif p1 + 1 < len(s1) and p2 + 1 < len(s2) and s1[p1 + 1] == s2[p2 + 1]:
                # We "replaced" a char in p1 or p2
                p1 += 1
                p2 += 1
            elif p1 + 1 < len(s1) and s1[p1 + 1] == s2[p2]:
                # We "removed" a char from p1
                p1 += 1
            elif p2 + 1 < len(s2) and s2[p2 + 1] == s1[p1]:
                # We "removed" a char from p2
                p2 += 1
            else:
                return False

            is_edited = True

        return (p1 == len(s1) and p2 == len(s2)) or ((not is_edited) and (len(s1) - p1 <= 1) and (len(s2) - p2 <= 1))
