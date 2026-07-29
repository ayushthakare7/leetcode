# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        def maxPathSum(self, root: Optional[TreeNode]) -> int:
            self.sum_node = float("-inf")
            def solve(root) :
                if root == None :
                    return 0
                left = solve(root.left)
                if left < 0:
                    left = 0
                right = solve(root.right)
                if right < 0:
                    right = 0
                self.sum_node = max(left + right + root.val, self.sum_node)
                return max(left,right) + root.val
            solve(root)
            return self.sum_node


        

        