# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(root):

            if root == None :
                return 0
            left_sum = solve(root.left)
            if left_sum == -1:
                return -1
            right_sum = solve(root.right)
            if right_sum == -1:
                return -1
            if abs(left_sum - right_sum) > 1:
                return -1
            return 1 + max(left_sum,right_sum)
           
            
            
        x =solve(root)
        if x == -1 :
            return False
        
        return True