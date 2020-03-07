class Solution:
    def sortByBits(self, nums):
        def f(x):
            s = str(bin(x)[2:])
            return s.count('1')

        arr = {num: [f(num), num] for num in nums}
        return sorted(nums, key=lambda x: arr[x])
