class StringCompression:
    """
    1.6
    String Compression: Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z).
    Hints:#92, #110
    """

    @staticmethod
    def compress(original):
        if original == '':
            return original

        # Compressed string characters
        compressed = []
        prev = None
        cnt = 0
        # compressed size - original size
        delta_size = 0

        for c in original:
            if prev is None:
                # Initial step
                prev = c
                cnt = 1
            elif c == prev:
                # Repeating character, continue
                cnt += 1
            else:
                # End chain of the same character, start new
                compressed.append(prev)
                str_cnt = str(cnt)
                compressed.append(str_cnt)
                delta_size += (cnt - len(str_cnt))
                prev = c
                cnt = 1

        # Add last uncompleted chain
        str_cnt = str(cnt)
        compressed.append(prev)
        compressed.append(str_cnt)
        delta_size += (cnt - len(str_cnt))

        # If the
        # "compressed" string would not become smaller than the original string, your method should return
        # the original string
        # if len(compressed) > len(original):
        if delta_size <= 0:
            compressed = original
        else:
            compressed = ''.join(compressed)

        return compressed
