class Solution:
    def minCostToMoveChips(self, chips):
        odd, even = 0, 0
        for chip in chips:
            if chip % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)
