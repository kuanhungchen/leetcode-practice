# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        # recursive solution
        ans = []
        if root is not None:
            ans.append(root.val)
            ans.extend(self.preorderTraversal(root.left))
            ans.extend(self.preorderTraversal(root.right))
        return ans


class Solution2:
    def preorderTraversal(self, root):
        ans, _stack = [], [root]
        while len(_stack) != 0:
            now = _stack.pop(-1)
            if now is not None:
                ans.append(now.val)
                _stack.append(now.right)
                _stack.append(now.left)
        return ans

