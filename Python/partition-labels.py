class Solution:
    def partitionLabels(self, S):

        lasts = {c: i for i, c in enumerate(S)}

        slow, fast = 0, 0
        ans = []

        while fast < len(S):
            dst = lasts[S[fast]]
            while fast < len(S) and fast != dst:
                fast += 1
                dst = max(lasts[S[fast]], dst)

            ans.append(fast - slow + 1)
            slow = fast = fast + 1

        return ans
