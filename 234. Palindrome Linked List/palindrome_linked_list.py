"""
Problem : 234. Palindrome Linked List
Difficulty: Easy
Topics   : Linked List, Two Pointers, Stack, Recursion
Runtime  : 17
Memory   : 53364000
Language : python3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        linked_list = []

        while curr:
            linked_list.append(curr.val)
            curr = curr.next

        return linked_list == linked_list[::-1]
