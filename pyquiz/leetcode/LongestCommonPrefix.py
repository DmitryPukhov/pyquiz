from typing import List


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Initial state
        prefix = list()
        cur_char = strs[0][0] if len(strs) > 0 and strs is not None and strs[0] is not None and len(
            strs[0]) > 0 else None
        i = 0
        is_common_char = True
        # Move pointer along all strings
        while cur_char is not None and is_common_char:
            # Get current char from first string as original
            cur_char = strs[0][i] if len(strs) > 0 and strs is not None and strs[0] is not None and i < len(
                strs[0]) else None

            is_common_char = cur_char is not None
            for cur_str in strs:
                if cur_str is None or not (i < len(cur_str) and cur_str[i] == cur_char):
                    # If not common char
                    is_common_char = False
                    break
                # If we are here, current char is present in all strings
            if is_common_char:
                prefix.append(cur_char)
            i += 1

        return ''.join(prefix)
