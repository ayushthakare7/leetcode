# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level = 0
        def solve(root,level):
            if root == None :
                return
            if len(ans) == level:
                ans.append(root.val)
           
            if root.right :
                solve(root.right, level + 1)
            if root.left :
                solve(root.left, level + 1)
            return ans
        solve(root,0)
        return ans



            

        