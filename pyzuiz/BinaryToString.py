class BinaryToString:
    """
    Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
    the binary representation. If the number cannot be represented accurately in binary with at most 32
    characters, print "ERROR:'
    """

    @staticmethod
    def to_string(float_num: float, base=2):
        numbers = []
        while float_num > 0:
            if len(numbers) >= 32:
                return "ERROR"

            cur_num = float_num * base
            numbers.append(int(cur_num))

            if cur_num >= 1:
                float_num = cur_num - 1
            else:
                float_num = cur_num

        return '0.' + ''.join(str(i) for i in numbers).rstrip('0')
