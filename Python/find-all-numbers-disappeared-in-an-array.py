class Solution:
    def findDisappearedNumbers(self,  nums):
        ans = []
        a = set(nums)
        for item in range(1, len(nums)+1):
            if item not in a:
                ans.append(item)
        return ans


class Solution2:
    # tricky method, roughly same speed
    def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums)+1)) - set(nums))
