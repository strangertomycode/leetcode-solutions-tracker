"""
Problem : 21. Merge Two Sorted Lists
Difficulty: Easy
Topics   : Linked List, Recursion
Runtime  : 0
Memory   : 19276000
Language : python3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l2.val < l1.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            
            head = head.next
        
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        
        return dummy.next
