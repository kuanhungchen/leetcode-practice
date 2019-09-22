class Solution:
    def nthUglyNumber(self, n, a, b, c):
        # use uglyNumBelow(x) to find the number of ugly numbers that are below x
        # use binary search to find the number x that uglyNumBelow(x) == n and it is divisible by at least one of a, b,c
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

        def uglyNumBelow(x):
            return x // a + x // b + x // c - x // lcm_ab - x // lcm_bc - x // lcm_ac + x // lcm_abc

        lcm_ab = lcm(a, b)
        lcm_bc = lcm(b, c)
        lcm_ac = lcm(a, c)
        lcm_abc = lcm(lcm_ab, lcm_bc)

        left = 1
        right = 2 * 10 ** 9
        while left + 1 < right:
            mid = (left + right) // 2
            uglyNum = uglyNumBelow(mid)
            if uglyNum == n:
                if mid % a == 0 or mid % b == 0 or mid % c == 0:
                    return mid
                else:
                    right = mid
            elif uglyNum > n:
                right = mid
            else:
                left = mid
