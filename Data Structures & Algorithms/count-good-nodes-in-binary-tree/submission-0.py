# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node:
                return 0
            good = 0

            if node.val >= maxSoFar:
                good = 1
            maxSoFar = max(node.val, maxSoFar)

            left = dfs(node.left, maxSoFar)
            right = dfs(node.right, maxSoFar)
            return good + left + right

        return dfs(root, root.val)
