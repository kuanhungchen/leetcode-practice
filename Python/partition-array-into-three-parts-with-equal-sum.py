class Solution:
    def canThreePartsEqualSum(self, A):
        _sum = sum(A)
        if _sum % 3 != 0:
            return False

        each = _sum // 3
        now = 0
        idx = 0
        for i in A:
            i += now
            if now == each:
                now = 0
                idx += 1
                if idx == 2:
                    return True
        return False
