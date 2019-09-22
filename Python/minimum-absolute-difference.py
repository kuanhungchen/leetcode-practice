class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        ans = []
        _min = 10 ** 13
        for idx in range(len(arr)-1):
            _min = min(_min, arr[idx+1]-arr[idx])
        for idx in range(len(arr)-1):
            if arr[idx+1]-arr[idx] == _min:
                ans.append([arr[idx], arr[idx+1]])
        return ans
