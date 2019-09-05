class Solution:
    def findDuplicate(self, nums):
        # O(n), O(n)
        from collections import Counter
        c = Counter(nums)
        return [x for x in c.keys() if c[x] > 1][0]


class Solution2:
    def findDuplicate(self, nums):
        # same as Solution
        # O(n), O(n)
        _dict = {}
        for num in nums:
            if num in _dict.keys():
                return num
            else:
                _dict[num] = 1


class Solution3:
    def findDuplicate(self, nums):
        # O(nlgn), O(1)
        # but the array should not be modified
        nums.sort()
        tmp = nums[-1]
        for num in nums:
            if num == tmp:
                return num
            tmp = num


class Solution4:
    def findDuplicate(self, nums):
        # Floyd's cycle detection algorithm
        # O(n), O(1)
        # not modify the array
        t, h = nums[0], nums[nums[0]]
        while t != h:
            t = nums[t]
            h = nums[nums[h]]
        t = 0
        while t != h:
            t = nums[t]
            h = nums[h]
        return t
