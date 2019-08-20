class Solution:
    def sortedSquares(self, A):
        # use a * a is faster than a ** 2
        if len(A) == 1: return [A[0] * A[0]]
        center = 0
        for i in range(1, len(A)):
            if abs(A[i]) <= abs(A[center]):
                center = i
            else:
                break

        ans = [A[center] * A[center]]
        left = center - 1
        right = center + 1
        while left != -1 and right != len(A):
            if abs(A[left]) < abs(A[right]):
                ans.append(A[left] * A[left])
                left -= 1
            else:
                ans.append(A[right] * A[right])
                right += 1
        if left == -1:  # right side remains
            while right != len(A):
                ans.append(A[right] * A[right])
                right += 1
        elif right == len(A):  # left side remains
            while left != -1:
                ans.append(A[left] * A[left])
                left -= 1
        return ans


class Solution2:
    # much faster than Solution
    # use a * a is faster than a ** 2
    def sortedSquares(self, A):
        ans = []
        for item in A:
            ans.append(item * item)
        ans.sort()

        return ans


class Solution3:
    # just for saving memory usage
    def sortedSquares(self, A):
        A = [item * item for item in A]
        A.sort()
        return A
