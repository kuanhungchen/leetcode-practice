# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def postorderTraversal(self, root):
        # recursive solution
        ans = []
        if root:
            ans.extend(self.postorderTraversal(root.left))
            ans.extend(self.postorderTraversal(root.right))
            ans.append(root.val)
        return ans


class Solution2:

    def postorderTraversal(self, root):
        # iterative, reverse the final answer!
        # copy from others
        ans, nodes = [], [root]
        while nodes:
            now = nodes.pop()
            if now:
                ans.append(now.val)
                nodes.append(now.left)
                nodes.append(now.right)
        return ans[::-1]
