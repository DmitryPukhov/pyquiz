class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a)
        lenb = len(b)
        maxlen = max(len(a), len(b))
        carry = 0
        res = []
        for i in range(maxlen):
            ai = lena - i - 1
            an = int(a[ai]) if ai >= 0 else 0
            bi = lenb - i - 1
            bn = int(b[bi]) if bi >= 0 else 0
            summ = an + bn + carry
            carry = summ // 2
            digit = summ % 2
            res.append(str(digit))
        if carry:
            res.append('1')
        summ = ''.join(reversed(res))
        return summ
