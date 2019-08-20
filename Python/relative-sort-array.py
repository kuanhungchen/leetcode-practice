class Solution:
    def relativeSortArray(self, arr1, arr2):
        idx = 0
        for target in arr2:
            for i in range(idx, len(arr1)):
                if arr1[i] == target:
                    arr1[i] = arr1[idx]
                    arr1[idx] = target
                    idx += 1

        tmp = sorted(arr1[idx:])
        ans = arr1[:idx] + tmp
        return ans


class Solution2:
    def relativeSortArray(self, arr1, arr2):
        # faster, freq dict
        freq = {x: 0 for x in arr2}
        other = []
        for num in arr1:
            if num in arr2:
                freq[num] += 1
            else:
                other.append(num)

        ans = []
        for num in arr2:
            ans += [num] * freq[num]

        other.sort()

        return ans + other
