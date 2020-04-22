# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, nums):
        def solve(node, value):
            if node.val > value and node.left is None:
                node.left = TreeNode(value)
            elif node.val > value and node.left is not None:
                solve(node.left, value)
            elif node.val < value and node.right is None:
                node.right = TreeNode(value)
            elif node.val < value and node.right is not None:
                solve(node.right, value)
            return node

        if not nums: return None
        ans = TreeNode(nums[0])
        res = ans
        for num in nums[1:]:
            if num < res.val:
                res = solve(res, num)
            else:
                res = solve(ans, num)
        return ans
