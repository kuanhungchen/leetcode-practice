class Solution:
    def wordSubsets(self, A, B):

        def solve(require, s):
            for k, v in require.items():
                if s.count(k) < v:
                    return False
            return True

        max_b = {}
        for b in B:
            b_dict = {}
            for x in b:
                if x in b_dict:
                    b_dict[x] += 1
                else:
                    b_dict[x] = 1
            for k, v in b_dict.items():
                max_b[k] = max(max_b[k], v) if k in max_b else v

        return [a for a in A if solve(max_b, a)]
