class Solution:
    def solveEquation(self, equation):

        def solve(hand):
            total_x = 0
            sm = 0
            num = ""
            op = 1
            for c in hand:
                if c == 'x':
                    total_x += int(num) * op if num != "" else 1 * op
                    num = ""
                elif c == '+':
                    if num != "":
                        sm += int(num) * op
                    op = 1
                    num = ""
                elif c == '-':
                    if num != "":
                        sm += int(num) * op
                    op = -1
                    num = ""
                else:
                    num += c
            if num != "":
                sm += int(num) * op
            return total_x, sm

        left, right = equation.split('=')
        left_xes, left_sm = solve(left)
        right_xes, right_sm = solve(right)

        left_xes, right_xes = left_xes - right_xes, 0
        left_sm, right_sm = 0, right_sm - left_sm
        if left_xes == 0:
            return "No solution" if right_sm != 0 else "Infinite solutions"
        return "x=" + str(right_sm // left_xes)
