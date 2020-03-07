class Solution:
    def countOrders(self, n: int) -> int:
        def fact(x):
            if x == 1: return 1
            return x * fact(x-1)
        return (fact(2*n) // (2**n)) % (10**9 + 7)
