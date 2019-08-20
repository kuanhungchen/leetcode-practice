class Solution:
    def sumEvenAfterQueries(self, A, queries):
        ans = []
        sum = 0
        for item in A:
            if item % 2 == 0:
                sum += item

        for query in queries:
            if A[query[1]] % 2 == 0:
                sum -= A[query[1]]
            A[query[1]] += query[0]
            if A[query[1]] % 2 == 0:
                sum += A[query[1]]
            ans.append(sum)

        return ans
