class Solution:
    # kind of dynamic programming?
    def fib(self, N):
        prepared_numbers = [0, 1, 1, 2, 3, 5, 8, 13]
        if N <= len(prepared_numbers) - 1:
            return prepared_numbers[N]
        else:
            for i in range(N - len(prepared_numbers) + 1):
                prepared_numbers.append(prepared_numbers[-2] + prepared_numbers[-1])
            return prepared_numbers[-1]
