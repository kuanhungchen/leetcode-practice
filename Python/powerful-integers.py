class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x, y = sorted([x, y], reverse=True)
        ans = {}
        if x == 1 and y == 1:
            return [2] if 2 <= bound else []
        elif y == 1:
            for i in range(100):
                if x ** i + 1 > bound: return ans.keys()
                ans[x ** i + 1] = 1
        i, j = 0, 0
        while x ** i + 1 <= bound:
            while x ** i + y ** j <= bound:
                if x ** i + y ** j not in ans:
                    ans[x ** i + y ** j] = 1
                j += 1
            i, j = i + 1, 0
        return ans.keys()
