class Solution:
    def countPrimeSetBits(self, L, R):
        ans = 0
        for num in range(L, R+1):
            num = bin(num)[2:]
            ones = num.count('1')
            if ones in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
                ans += 1
        return ans


class Solution2:
    def countPrimeSetBits(self, L, R):
        # one line
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        return [True if bin(x)[2:].count('1') in primes else False for x in range(L, R+1)].count(True)
