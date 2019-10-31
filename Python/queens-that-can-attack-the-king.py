class Solution:
    def queensAttacktheKing(self, queens, k):
        def solve(q, k):
            if q[0] == k[0]:
                return 1
            elif q[1] == k[1]:
                return 2
            for n in range(8):
                if (k[0] - n == q[0] and k[1] - n == q[1]) or (k[0] + n == q[0] and k[1] + n == q[1]):
                    return 3
                elif (k[0] - n == q[0] and k[1] + n == q[1]) or (k[0] + n == q[0] and k[1] - n == q[1]):
                    return 4
            return -1

        row = []
        column = []
        leftup = []
        rightup = []
        for queen in queens:
            res = solve(queen, k)
            if res == -1:
                continue
            if res == 1:
                row.append(queen)
            elif res == 2:
                column.append(queen)
            elif res == 3:
                leftup.append(queen)
            elif res == 4:
                rightup.append(queen)
        _closest = 10
        ans = []
        row.sort(key=lambda x: x[1])
        for q in row:
            if q[1] < k[1]:
                if k[1] - q[1] < _closest:
                    _closest = k[1] - q[1]
            elif q[1] > k[1]:
                if _closest != 10:
                    ans.append([k[0], k[1] - _closest])
                    _closest = 10
                ans.append([k[0], q[1]])
                break
        if _closest != 10:
            ans.append([k[0], k[1] - _closest])
        _closest = 10
        column.sort(key=lambda x: x[0])
        for q in column:
            if q[0] < k[0]:
                if k[0] - q[0] < _closest:
                    _closest = k[0] - q[0]
            elif q[0] > k[0]:
                if _closest != 10:
                    ans.append([k[0] - _closest, k[1]])
                    _closest = 10
                ans.append([q[0], k[1]])
                break
        if _closest != 10:
            ans.append([k[0] - _closest, k[1]])
        _closest = 10
        leftup.sort(key=lambda x: x[1])
        for q in leftup:
            if q[1] < k[1]:
                if k[1] - q[1] < _closest:
                    _closest = k[1] - q[1]
            elif q[1] > k[1]:
                if _closest != 10:
                    ans.append([k[0] - _closest, k[1] - _closest])
                    _closest = 10
                ans.append([q[0], q[1]])
                break
        if _closest != 10:
            ans.append([k[0] - _closest, k[1] - _closest])
        _closest = 10
        rightup.sort(key=lambda x: x[1])
        for q in rightup:
            if q[1] < k[1]:
                if k[1] - q[1] < _closest:
                    _closest = k[1] - q[1]
            elif q[1] > k[1]:
                if _closest != 10:
                    ans.append([k[0] + _closest, k[1] - _closest])
                    _closest = 10
                ans.append([q[0], q[1]])
                break
        if _closest != 10:
            ans.append([k[0] + _closest, k[1] - _closest])

        return ans
