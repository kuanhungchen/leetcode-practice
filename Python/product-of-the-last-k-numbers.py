class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.pds = [1]
        self.last_zero = None

    def add(self, num):
        self.arr.append(num)
        if num == 0:
            self.last_zero = len(self.arr) - 1
            self.pds.append(self.pds[-1])
        else:
            self.pds.append(self.pds[-1] * num)

    def getProduct(self, k):
        if self.last_zero is None or len(self.arr) - self.last_zero > k:
            return self.pds[-1] // self.pds[len(self.arr) - k]
        return 0
