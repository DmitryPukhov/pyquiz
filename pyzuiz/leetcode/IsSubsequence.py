class IsSubsequence:
    def isSubsequence(self, s: str, t: str) -> bool:
        pt1 = 0
        for ss in s:
            found = False
            for pt in range(pt1, len(t)):
                if t[pt] == ss:
                    # Found
                    found = True
                    pt1 = pt
                    break

            if not found:
                # Didn't find current letter
                return False
        return True
