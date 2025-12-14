# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, p: Optional[TreeNode], val: int) -> bool:
        if not p:
            return False
        if not p.right and not p.left:
            if p.val == val:
                return True
            return False
        val -= p.val
        return (self.hasPathSum(p.left, val) or self.hasPathSum(p.right, val))

