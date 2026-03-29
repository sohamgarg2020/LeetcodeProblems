# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divideAndConquer(lists, 0, len(lists) - 1)

    def divideAndConquer(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]

        mid = (left + right) // 2
        l1 = self.divideAndConquer(lists, left, mid)
        l2 = self.divideAndConquer(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2) 
        
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next
        dummy.next = list1 if list1 else list2
        return cur.next
