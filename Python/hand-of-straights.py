class Solution:
    def isNStraightHand(self, cards, W):
        cards.sort()
        while len(cards):
            if len(cards) < W:
                return False
            l = 1
            last = cards.pop(-1)
            re = []
            while l != W:
                if len(cards) == 0:
                    return False
                now = cards.pop(-1)
                if now == last:
                    re.append(now)
                elif now == last - 1:
                    l += 1
                    last = now
                else:
                    return False
            cards.extend(reversed(re))
        return True
