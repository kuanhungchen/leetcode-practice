class Solution:
    def isAnagram(self, s, t):
        s = sorted([x for x in s])
        s_dict = {}
        for char in s:
            if char in s_dict.keys():
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char not in s_dict.keys():
                return False
            s_dict[char] -= 1
            if s_dict[char] == 0:
                s_dict.pop(char)

        return len(s_dict) == 0


class Solution2:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


class Solution3:
    def isAnagram(self, s, t):
        # faster
        s_dict = {}
        for char in s:
            if char in s_dict.keys():
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char not in s_dict.keys():
                return False
            s_dict[char] -= 1
            if s_dict[char] == 0:
                s_dict.pop(char)

        return len(s_dict) == 0


class Solution4:
    def isAnagram(self, s, t):
        # much faster
        from collections import Counter
        s_dict = Counter(s)
        t_dict = Counter(t)
        if len(s_dict) != len(t_dict):
            return False
        for char in s_dict:
            if s_dict[char] != t_dict[char]:
                return False
        return True
