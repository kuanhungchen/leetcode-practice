class Solution:
    def circularArrayLoop(self, nums):
        # brutal force solution
        # use _no to speed up (skip failed num)
        if not nums:
            return False
        _no = []
        _c = 0
        slow, fast = _c, (_c + nums[_c] + len(nums)) % len(nums)
        _dir = 1 if nums[_c] > 0 else -1
        _dict = {slow: 1}
        while True:
            if (nums[fast] > 0 and _dir == -1) or (nums[fast] < 0 and _dir == 1):
                _no.extend(_dict.keys())
                while _c in _no:
                    _c += 1
                    if _c == len(nums):
                        return False
                slow, fast = _c, (_c + nums[_c] + len(nums)) % len(nums)
                _dir = 1 if nums[_c] > 0 else -1
                _dict = {slow: 1}
                continue
            slow, fast = fast, (fast + nums[fast] + len(nums)) % len(nums)
            if slow in _dict.keys():
                if slow != fast:
                    return True
                _no.extend(_dict.keys())
                while _c in _no:
                    _c += 1
                    if _c == len(nums):
                        return False
                slow, fast = _c, (_c + nums[_c] + len(nums)) % len(nums)
                _dir = 1 if nums[_c] > 0 else -1
                _dict = {slow: 1}
                continue
            else:
                _dict[slow] = 1
