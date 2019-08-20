class Solution:
    def findMaxConsecutiveOnes(self, nums):
        _max = 0
        cnt = 0
        for i in nums:
            if i:
                cnt += 1
            else:
                cnt = 0

            _max = max(_max, cnt)
        return _max


class Solution2:
    # a bit faster
    def findMaxConsecutiveOnes(self, nums):
        idx = 0
        tmp = 0
        _max = 0
        while True:
            try:
                idx = nums.index(0, tmp)
            except ValueError:
                break
            length = idx - tmp
            _max = max(_max, length)
            tmp = idx + 1

        if idx == 0:
            return sum(nums)
        length = len(nums) - idx - 1
        _max = max(_max, length)
        return _max


sln = Solution2()
print(sln.findMaxConsecutiveOnes([0]))
