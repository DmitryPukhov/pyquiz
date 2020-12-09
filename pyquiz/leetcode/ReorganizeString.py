import collections


class ReorganizeString:
    """
    Given a string S, check if the letters can be rearranged
    so that two characters that are adjacent to each other are not the same.
    If possible, output any possible result.  If not possible, return the empty string.

    Example 1:
    Input: S = "aab"
    Output: "aba"

    Example 2:
    Input: S = "aaab"
    Output: ""

    Note:
    S will consist of lowercase letters and have length in range [1, 500].
    """
    def reorganizeString(self, S: str) -> str:
        sortedcommons = []
        lens = len(S)
        for c, cnt in collections.Counter(S).most_common()[::-1]:
            if cnt > (lens + 1) // 2:
                return ""
            sortedcommons.extend([c] * cnt)

        out = [None] * lens
        out[::2] = sortedcommons[lens // 2:]
        out[1::2] = sortedcommons[:lens // 2]
        return "".join(out)
