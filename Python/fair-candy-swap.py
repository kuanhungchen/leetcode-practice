class Solution:
    def fairCandySwap(self, A, B):
        # Time Limit Exceeded
        difference = sum(B) - sum(A)
        for i in A:
            for j in B:
                if 2 * (j - i) == difference:
                    return [i, j]


class Solution2:
    def fairCandySwap(self, A, B):
        # still slow
        sum_A = sum(A)
        sum_B = sum(B)
        difference = (sum_B - sum_A) // 2
        for item in A:
            if item + difference in B:
                return [item, item+difference]


class Solution3:
    def fairCandySwap(self, A, B):
        # much faster
        difference = (sum(B) - sum(A)) // 2
        A = set(A)
        B = set(B)
        for item in A:
            if item + difference in B:
                return [item, item + difference]
