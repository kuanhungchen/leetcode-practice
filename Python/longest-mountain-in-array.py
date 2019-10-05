class Solution:
    def longestMountain(self, A):
        slow = fast = 0
        max_len = 0
        while fast < len(A):
            while fast < len(A) and A[fast] <= A[slow]:
                slow = fast
                fast += 1
            last = A[slow]
            while fast < len(A) and A[fast] > last:
                last = A[fast]
                fast += 1
            if fast == len(A):
                break
            if A[fast] == last:
                slow = fast
                continue
            while fast < len(A) and A[fast] < last:
                last = A[fast]
                fast += 1
            max_len = max(max_len, fast-slow)
            slow = fast-1
        return max_len
