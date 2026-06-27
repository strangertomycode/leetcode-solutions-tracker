"""
Problem : 234. Palindrome Linked List
Difficulty: Easy
Topics   : Linked List, Two Pointers, Stack, Recursion
Runtime  : 39
Memory   : 42720000
Language : python3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # curr = head
        # linked_list = []

        # while curr:
        #     linked_list.append(curr.val)
        #     curr = curr.next

        # return linked_list == linked_list[::-1]

        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next
        
        prev = None
        curr = s

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        left = head
        right = prev

        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        
        return True

