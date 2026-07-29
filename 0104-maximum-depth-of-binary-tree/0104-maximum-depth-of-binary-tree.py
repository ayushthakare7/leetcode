# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        
        left_sum = self.maxDepth(root.left)
        r_sum = self.maxDepth(root.right) 
        max_sum = max(left_sum, r_sum)
        return max_sum + 1
        

        
        
        