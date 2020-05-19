class ListNode:
    def __init__(self, val=0, less=0, pre=None):
        self.val = val
        self.less = less
        self.pre = pre


class StockSpanner:

    def __init__(self):
        self.tail = ListNode(val=10 ** 6)

    def next(self, price):
        total, cur = 1, self.tail
        while cur and cur.val <= price:
            total += cur.less
            cur = cur.pre
        self.tail = ListNode(price, total, cur)
        return total


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
