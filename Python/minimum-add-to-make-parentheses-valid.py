class Solution:
    def minAddToMakeValid(self, S):
        left_need, right_need = 0, 0
        for c in S:
            if c == '(': right_need += 1
            elif c == ')' and right_need != 0: right_need -= 1
            else: left_need += 1
        return left_need + right_need
