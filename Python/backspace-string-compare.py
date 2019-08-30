class Solution:
    def backspaceCompare(self, S, T):
        # stack method
        stack_s = []
        for char in S:
            if char == '#':
                if len(stack_s) > 0:
                    stack_s.pop()
            else:
                stack_s.append(char)
        stack_t = []
        for char in T:
            if char == '#':
                if len(stack_t) > 0:
                    stack_t.pop()
            else:
                stack_t.append(char)
        return stack_s == stack_t


class Solution2:
    def backspaceCompare(self, S, T):
        idx_s = len(S)-1
        idx_t = len(T)-1
        while True:
            pound_count = S[idx_s].count('#')
            char_count = 1 - pound_count
            while char_count - pound_count != 1:
                idx_s -= 1
                if idx_s < 0:
                    break
                pound_count += S[idx_s].count('#')
                char_count += 1 - S[idx_s].count('#')

            pound_count = T[idx_t].count('#')
            char_count = 1 - pound_count
            while char_count - pound_count != 1:
                idx_t -= 1
                if idx_t < 0:
                    break
                pound_count += T[idx_t].count('#')
                char_count += 1 - T[idx_t].count('#')
            if idx_s >= 0 and idx_t >= 0:
                if S[idx_s] != T[idx_t]:
                    return False
                idx_s -= 1
                idx_t -= 1
            else:
                return idx_s < 0 and idx_t < 0
