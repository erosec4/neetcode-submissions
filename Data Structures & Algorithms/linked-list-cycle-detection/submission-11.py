# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Edge case: no head
        if head:
            i = head
        else:
            return False

        # Edge case: length of 1
        if head.next:
            j = head.next
        else:
            return False

        while j != i:
            if not j.next or not j.next.next:
                return False
            i = i.next
            j = j.next.next
        return True
        