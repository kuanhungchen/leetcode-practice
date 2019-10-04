class Solution:

    def solve(self, spcl_idx, nds, cost, _min):
        if spcl_idx == len(self._specials):
            for i, nd in enumerate(nds):
                cost += nd * self._prices[i]
            return cost

        spcl = self._specials[spcl_idx]
        n = 0
        flag = True
        while flag:
            n += 1
            for i, s in enumerate(spcl[:-1]):
                if s * n > nds[i]:
                    flag = False
                    break

        for i in range(n):
            new_nds = [nd - s * i for nd, s in zip(nds, spcl[:-1])]
            if i != 0:
                cost += spcl[-1]
            _min = min(self.solve(spcl_idx + 1, new_nds, cost, _min), _min)

        return _min

    def shoppingOffers(self, prices, specials, needs):
        self._prices = prices
        self._specials = specials
        self._needs = needs

        return self.solve(0, needs, 0, 10 ** 9)
