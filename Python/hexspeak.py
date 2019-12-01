class Solution:
    def toHexspeak(self, num: str) -> str:
        ans = ""
        mapping = {'0': 'O', '1': 'I', 'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
        for c in str(hex(int(num)).split('x')[-1]):
            if c not in mapping: return "ERROR"
            ans += mapping[c]
        return ans
