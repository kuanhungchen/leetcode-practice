class Solution:
    def sortArrayByParityII(self, A):
        odds = []
        evens = []
        for item in A:
            if item % 2 == 0: evens.append(item)
            else: odds.append(item)

        ans = []
        for i in range(len(odds)):
            ans.append(evens[i])
            ans.append(odds[i])
        return ans


class Solution2:
    # tricky method
    def sortArrayByParityII(self, A):
        ans = [0] * len(A)
        even_idx = 0
        odd_idx = 1
        for item in A:
            if item % 2 == 0:
                ans[even_idx] = item
                even_idx += 2
            else:
                ans[odd_idx] = item
                odd_idx += 2
        return ans
