# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start_node = ListNode()
        tail = start_node

        # Compare and add to new linked list after start_node
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Check if either list still has nodes
        if list1:
            tail.next = list1
            '''list1 = list1.next
            tail = tail.next''' # Don't need to add each node; already linked
        if list2:
            tail.next = list2

        return start_node.next
        

                
        