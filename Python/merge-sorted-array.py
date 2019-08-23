class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        _compare = [10000]
        for idx in range(m):
            _min = min(nums1[idx], _compare[0], nums2[0])
            if _min == nums1[idx]:
                pass
            elif _min == _compare[0]:
                _compare.append(nums1[idx])
                nums1[idx] = _compare.pop(0)
            else:
                _compare.append(nums1[idx])
                nums1[idx] = nums2.pop(0)
            if 10000 in _compare and len(_compare) != 1:
                _compare.remove(10000)
            if not nums2:
                nums2.append(10000)
        _compare = _compare + nums2
        _compare.sort()
        for idx in range(n):
            nums1[m+idx] = _compare.pop(0)


class Solution2:
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return
        for idx in range(m):
            if nums1[idx] < nums2[0]:
                continue
            else:
                nums2.append(nums1[idx])
                nums1[idx] = nums2.pop(0)
                nums2.sort()
        for idx in range(n):
            nums1[idx+m] = nums2.pop(0)


class Solution3:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m]+nums2)


class Solution4:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
