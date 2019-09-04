class Solution:
    def findDuplicate(self, nums):
        # O(n), O(n)
        from collections import Counter
        c = Counter(nums)
        return [x for x in c.keys() if c[x] > 1][0]


class Solution2:
    def findDuplicate(self, nums):
        # O(n), O(n)
        _dict = {}
        for num in nums:
            if num in _dict.keys():
                return num
            else:
                _dict[num] = 1


class Solution3:
    def findDuplicate(self, nums):
        # O(nlgn) if quick sort, O(1)
        nums.sort()
        tmp = nums[-1]
        for num in nums:
            if num == tmp:
                return num
            tmp = num
