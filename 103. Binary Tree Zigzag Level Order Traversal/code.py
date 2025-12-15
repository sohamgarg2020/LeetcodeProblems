from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        cur = []
        check = 0

        while q:
            num = len(q)
            ret = []
            for i in range(num):
                node = q.popleft()
                ret.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if check % 2 == 1:
                ret = ret[::-1]            
            check += 1
            cur.append(ret)
        return cur
