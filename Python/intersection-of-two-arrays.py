class Solution:
    def intersection(self, nums1, nums2):
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        ans = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    ans.append(num2)

        return ans


class Solution2:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1) > len(nums2):
            return [x for x in nums1 if x in nums2]
        else:
            return [x for x in nums2 if x in nums1]
