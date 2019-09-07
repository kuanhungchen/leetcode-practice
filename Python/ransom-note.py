class Solution:
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter
        return [Counter(magazine)[ch] >= Counter(ransomNote)[ch] for ch in Counter(ransomNote)].count(True) == len(Counter(ransomNote))


class Solution2:
    def canConstruct(self, ransomNote, magazine):
        magazine_map = {}
        for x in magazine:
            if x in magazine_map:
                magazine_map[x] += 1
            else:
                magazine_map[x] = 1
        ransomNote_map = {}
        for x in ransomNote:
            if x in ransomNote_map:
                ransomNote_map[x] += 1
            else:
                ransomNote_map[x] = 1

        for k, v in ransomNote_map.items():
            if k not in magazine_map or magazine_map[k] < v:
                return False
        return True
