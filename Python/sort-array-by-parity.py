class Solution:
    def sortArrayByParity(self, A):
        ans = []
        for idx in range(2):
            for item in A:
                if item % 2 == idx: ans.append(item)  # idx = 0 for even, 1 for odd
        return ans


class Solution2:
    # this method traverses array only once
    def sortArrayByParity(self, A):
        odds = []
        evens = []
        for item in A:
            if item % 2 == 0: evens.append(item)
            else: odds.append(item)
        evens.extend(odds)
        return evens
