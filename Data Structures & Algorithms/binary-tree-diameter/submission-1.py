# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def function_dfs(node):
            nonlocal res
            
            if not node:
                return 0
            
            left = function_dfs(node.left)
            right = function_dfs(node.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        function_dfs(root)
        return res

            