class Solution:
    def findMinFibonacciNumbers(self, k):
        arr = [1, 1]
        while arr[-1] < k:
            tmp = arr[-1] + arr[-2]
            arr.append(tmp)

        ans = 0
        for num in reversed(arr):
            if num <= k:
                k -= num
                ans += 1
                if k == 0: return ans


class Solution2:
    def findMinFibonacciNumbers(self, k):
        arr = [1, 1]
        while arr[-1] < k:
            tmp = arr[-1] + arr[-2]
            arr.append(tmp)
        def bs(start, end, tar):
            l, r = start, end
            while l + 1 < r:
                m = (l + r) // 2
                if arr[m] == tar:
                    return 1
                if arr[m] < tar < arr[m + 1]:
                    return 1 + bs(start, m, tar - arr[m])
                elif arr[m] > tar:
                    r = m
                else:
                    l = m
            return 1
        if arr[-1] == k: return 1
        return 1 + bs(0, len(arr) - 2, k - arr[-2])
