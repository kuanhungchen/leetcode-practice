# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        def solve(node, path, ans):
            if not node.left and not node.right:
                ans.append(path)
            if node.left:
                ans = solve(node.left, path + "->" + str(node.left.val), ans)
            if node.right:
                ans = solve(node.right, path + "->" + str(node.right.val), ans)
            return ans

        return [] if not root else solve(root, str(root.val), [])
