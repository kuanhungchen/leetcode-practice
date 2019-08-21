class Solution:
    def addToArrayForm(self, A, K):
        # copy from others
        result = []
        carry = K
        for digit in A[::-1]:
            _new = digit + carry
            result.append(_new % 10)
            carry = _new // 10
        while carry:
            result.append(carry % 10)
            carry //= 10

        return result[::-1]
