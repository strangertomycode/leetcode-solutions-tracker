"""
Problem : 141. Linked List Cycle
Difficulty: Easy
Topics   : Hash Table, Linked List, Two Pointers
Runtime  : 63
Memory   : 22564000
Language : python3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = set()
        # curr = head
        # while curr:
        #     if curr not in visited:
        #         visited.add(curr)
        #         curr = curr.next
        #     else:
        #         return True
        
        # return False

        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s:
                return True
        
        return False



