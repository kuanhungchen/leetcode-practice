# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        # recursive solution
        ans = []
        if root is not None:
            ans.extend(self.inorderTraversal(root.left))
            ans.extend([root.val])
            ans.extend(self.inorderTraversal(root.right))
        return ans


class Solution2:
    def inorderTraversal(self, root):
        # iterative solution
        # copy from others
        ans, _stack = [], [root]
        now = root
        while len(_stack) != 0 or now:
            while now:
                _stack.append(now)
                now = now.left
            now = _stack.pop(-1)
            ans.append(now.val)
            now = now.right
        return ans


class Solution3:
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
