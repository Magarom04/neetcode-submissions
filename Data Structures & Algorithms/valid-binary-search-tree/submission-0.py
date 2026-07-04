# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left, right):

            if not node:
                return True
            if not (left < node.val < right):
                return False

            leftTree = dfs(node.left, left, node.val)
            rightTree = dfs(node.right, node.val, right)

            return leftTree and rightTree

        return dfs(root, float("-inf"), float("inf"))
