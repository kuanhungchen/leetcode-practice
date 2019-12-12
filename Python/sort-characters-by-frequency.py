class Solution:
    def frequencySort(self, s):
        freqs = {}
        for c in s:
            if c not in freqs:
                freqs[c] = 1
            else:
                freqs[c] += 1

        ans = ""
        for k, v in sorted(freqs.items(), key=lambda x: x[1]):
            ans += k * v
        return ans[::-1]
