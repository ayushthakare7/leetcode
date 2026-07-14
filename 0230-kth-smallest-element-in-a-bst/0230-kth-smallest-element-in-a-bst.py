# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root

        while curr:
            if curr.left is None:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                # Find inorder predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if pred.right is None:
                    # Create thread
                    pred.right = curr
                    curr = curr.left
                else:
                    # Remove thread
                    pred.right = None

                    k -= 1
                    if k == 0:
                        return curr.val

                    curr = curr.right