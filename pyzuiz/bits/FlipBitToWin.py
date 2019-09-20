class FlipBitToWin:
    """
    You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
    find the length of the longest sequence of ls you could create.
    EXAMPLE
    Input: 1775
    Output: 8
    (or: 11
    """

    @staticmethod
    def longest_seq(x):
        flip_flag = False
        max_len = 0
        cur_len = 0
        last_chunk_len = 0
        for i in range(0, 32):
            mask = 1 << i
            is_bit_set = x & mask
            if not is_bit_set:
                # We found 0
                if not flip_flag:
                    # If first flip, just set flag and continue
                    flip_flag = True
                    cur_len += 1
                    last_chunk_len += 1
                    if cur_len > max_len:
                        max_len = cur_len
                    continue

                if cur_len > max_len:
                    # Update max seq len if current len is above
                    max_len = cur_len

                # Flip this bit instead of previous flip
                # Current length will be length of last 111 seq
                cur_len = last_chunk_len
                last_chunk_len = 1
            else:
                # We found 1, just continue and increase cur len
                cur_len += 1
                last_chunk_len += 1
                if cur_len > max_len:
                    max_len = cur_len

        if not flip_flag:
            # Use flip bit if we did not
            max_len += 1
        return max_len
