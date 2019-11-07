class Solution:
    def findTarget(self, root, k):
        def traversal(node, _k, _d):
            if not node: return
            if _k - node.val in _d: return True
            _d[node.val] = 1
            return traversal(node.left, _k, _d) or traversal(node.right, _k, _d)

        return traversal(root, k, {})
