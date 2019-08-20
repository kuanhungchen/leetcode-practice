class Solution:
    def intersect(self, nums1, nums2):
        ans = []
        for num in nums1:
            if num not in ans:
                for _ in range(min(nums1.count(num), nums2.count(num))):
                    ans.append(num)

        return ans


class Solution2:
    def intersect(self, nums1, nums2):
        freq = {}
        ans = []
        for num in nums1:
            if num in freq.keys():
                freq[num][0] += 1
            else:
                freq[num] = [1, 0]
        for num in nums2:
            if num in freq.keys():
                freq[num][1] += 1
            else:
                freq[num] = [0, 1]

        for k, v in freq.items():
            ans.extend([k] * min(v))

        return ans


class Solution3:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        ans = []
        i = j = 0

        while i < len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    while i < len(nums1) and nums1[i] < nums2[j]:
                        i += 1
                else:
                    while j < len(nums2) and nums2[j] < nums1[i]:
                        j += 1
        return ans
