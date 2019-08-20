class Solution:
    def numEquivDominoPairs(self, dominoes):
        occured = {}
        for domino in dominoes:
            if repr(domino) in occured.keys():
                occured[repr(domino)] += 1
            elif repr(domino[::-1]) in occured.keys():
                occured[repr(domino[::-1])] += 1
            else:
                occured[repr(domino)] = 1

        _sum = 0
        for freq in occured.values():
            _sum += (freq * (freq-1)) // 2
        return _sum


class Solution2:
    def numEquivDominoPairs(self, dominoes):
        occured = {}
        _sum = 0
        for domino in dominoes:
            if repr(domino) in occured.keys():
                _sum += occured[repr(domino)]
                occured[repr(domino)] += 1
            elif repr(domino[::-1]) in occured.keys():
                _sum += occured[repr(domino[::-1])]
                occured[repr(domino[::-1])] += 1
            else:
                occured[repr(domino)] = 1

        return _sum
