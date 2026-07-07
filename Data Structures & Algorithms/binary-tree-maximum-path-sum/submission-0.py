# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize global maximum with negative infinity to handle all-negative trees
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # Recursively compute the maximum path sum of left and right subtrees
            # Clamp negative contributions to 0 (ignore paths that lower the overall sum)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Price of the current path if this node acts as the highest "turning point"
            current_path_sum = node.val + left_gain + right_gain

            # Update the global maximum path sum encountered so far
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the single maximum branch gain to the parent node
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
