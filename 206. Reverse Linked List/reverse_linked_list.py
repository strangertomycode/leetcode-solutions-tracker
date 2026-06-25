"""
Problem : 206. Reverse Linked List
Difficulty: Easy
Topics   : Linked List, Recursion
Runtime  : 541
Memory   : 27028000
Language : python3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        print(curr)

        while curr:
            temp = curr.next
            curr.next = prev
            prev =  curr
            curr = temp
        
        return prev
