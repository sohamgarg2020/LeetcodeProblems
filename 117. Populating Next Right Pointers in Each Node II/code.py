from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        while q:
            rightNode = None
            nums = len(q)
            for i in range(nums):
                node = q.popleft()
                node.next, rightNode = rightNode, node
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root
