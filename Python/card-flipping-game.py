class Solution:
    def flipgame(self, fronts, backs):
        all_cards = list(set(fronts + backs))
        all_cards.sort()

        for m in all_cards:
            flag = True
            for f, b in zip(fronts, backs):
                if f == m and b == m:
                    flag = False
                    break
            if flag:
                return m
        return 0
