class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head, root):
        def dfs2(head, root):
            if not head: return True
            if not root: return False
            if head.val != root.val: return False
            return dfs2(head.next, root.left) or dfs2(head.next, root.right)

        def dfs(head, root):
            if not head: return True
            if not root: return False
            return dfs2(head, root) or dfs(head, root.left) or dfs(head, root.right)

        return dfs(head, root)
