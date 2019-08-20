class Solution:
    def containsDuplicate(self, nums):
        return sorted(list(set(nums))) != sorted(nums)


class Solution2:
    # only need to compare length, a little faster
    def containsDuplicate(self, nums):
        return len(list(set(nums))) != len(nums)


class Solution3:
    # more hash table concept
    def containsDuplicate(self, nums):
        from collections import defaultdict
        c = defaultdict(int)
        for num in nums:
            if num not in c:
                c[num] = 1
            else:
                return True
        return False
