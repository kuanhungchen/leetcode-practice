class Solution:
    def duplicateZeros(self, arr):
        for idx in range(len(arr)-1, -1, -1):
            if arr[idx] == 0:
                for j in range(len(arr)-2, idx-1, -1):
                    arr[j+1] = arr[j]


class Solution2:
    # much faster
    def duplicateZeros(self, arr):
        num, num_of_zeros = 0, 0
        while num + num_of_zeros < len(arr):
            if arr[num] == 0:
                num_of_zeros += 1
            num += 1
        now = len(arr) - 1
        if num + num_of_zeros > len(arr):
            arr[-1] = 0
            now = len(arr) - 2
            num -= 1

        num -= 1
        while num >= 0:
            if arr[num] == 0:
                arr[now] = 0
                now -= 1
            arr[now] = arr[num]
            num -= 1
            now -= 1
