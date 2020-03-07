class Cashier:

    def __init__(self, n, discount, products, prices):
        self.n = n
        self.now = n
        self.dc = discount
        self.pds = products
        self.pcs = prices

    def getBill(self, product, amount):
        money = 0
        for i in range(len(product)):
            money += self.pcs[self.pds.index(product[i])] * amount[i]

        self.now -= 1
        if self.now == 0:
            money = money - (self.dc * money) / 100
            self.now = self.n
        return money
