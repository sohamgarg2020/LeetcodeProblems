from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])
        seen_null = False

        while q:
            node = q.popleft()
            if node is None:
                seen_null = True
            else:
                if seen_null:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
