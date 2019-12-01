class Solution:
    def deckRevealedIncreasing(self, cards):
        cards = sorted(cards, reverse=True)
        ans = [cards[0]]
        for card in cards[1:]:
            ans = [card] + [ans[-1]] + ans[:-1]
        return ans
