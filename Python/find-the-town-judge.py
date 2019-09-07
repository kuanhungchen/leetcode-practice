class Solution:
    def findJudge(self, N, trust):
        if N == 1:
            return 1
        _trusts = []
        for _ in range(N+1):
            _trusts.append([])
        for r in trust:
            if r[1] not in _trusts[r[0]]:
                _trusts[r[0]].append(r[1])

        possibles = []
        for idx in range(len(_trusts)):
            if len(_trusts[idx]) == 0:
                possibles.append(idx)
        for idx in range(len(_trusts)):
            if idx in possibles:
                continue
            for i in range(len(possibles)):
                if possibles[i] not in _trusts[idx]:
                    possibles[i] = -1
            if sum(possibles) == -1 * len(possibles):
                return -1
        return sum(possibles) - (-1 * len(possibles)) - 1


class Solutio2:
    def findJudge(self, N, trust):
        if N == 1:
            return 1
        impossibles = []
        possibles = {}
        for t in trust:
            if t[0] not in impossibles:
                impossibles.append(t[0])

            if t[1] in impossibles:
                continue
            if t[1] not in possibles.keys():
                possibles[t[1]] = 1
            else:
                possibles[t[1]] += 1
        if not possibles.keys() or len(impossibles) == N:
            return -1
        to_be_checks = list(set(possibles.keys()) - set(impossibles))
        if not to_be_checks:
            return -1
        for to_be_check in to_be_checks:
            if possibles[to_be_check] == N-1:
                return to_be_check
        return -1


class Solution3:
    def findJudge(self, N, trust):
        possibles = {x: 0 for x in range(1, N+1)}
        for t in trust:
            possibles[t[0]] = -1
            if possibles[t[1]] != -1:
                possibles[t[1]] += 1
        return max([k if v == N-1 else -1 for k, v in possibles.items()])
