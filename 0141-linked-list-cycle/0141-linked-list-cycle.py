# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# check if node is not in hashmap
"""
While next node is not in hashmap
Add node to hashmap
if next node is none 
return false, meaning there's no cycle
update pointer outside if else

once we break out of while, return true, there's cycle

initialize two pointers at head
while pointerB.next.next != pointerA
if B.next.next == None or A.next == None: return False
increase the traversal by 1 for A and 2 for B

breaking, return True
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashmap = {}

        # if head == None: return False

        # while head.next not in hashmap:
        #     hashmap[head.next] = head.val
        #     if head.next == None: 
        #         return False
        #     head = head.next
        
        # return True

        pointerA = head
        pointerB = head

        if head == None: return False
        if head.next == None or pointerB.next.next == None: return False

        while pointerB and pointerA and pointerB.next:
            pointerA = pointerA.next
            pointerB = pointerB.next.next
        
            if pointerB == pointerA: return True
        return False

