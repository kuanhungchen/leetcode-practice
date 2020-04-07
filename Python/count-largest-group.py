class Solution:
    def countLargestGroup(self, A):
        mp = {}
        for num in range(1, A + 1):
            sm = sum([int(c) for c in str(num)])
            if sm not in mp:
                mp[sm] = 1
            else:
                mp[sm] += 1
        max_value, max_ele = 0, 0
        for k, v in mp.items():
            if v > max_value:
                max_value = v
                max_ele = 1
            elif v == max_value:
                max_ele += 1
        return max_ele
