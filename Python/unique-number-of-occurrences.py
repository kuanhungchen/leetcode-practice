class Solution:
    def uniqueOccurrences(self, arr):
        _dict = {}
        for num in arr:
            if num in _dict.keys():
                _dict[num] += 1
            else:
                _dict[num] = 1
        _occurence = list(_dict.values())
        return len(_occurence) == len(set(_occurence))
