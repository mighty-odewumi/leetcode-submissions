# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# For hashmap solution having both O(n) time and space complexities
"""
While next node is not in hashmap
Add node to hashmap
if next node is none 
return false, meaning there's no cycle
update pointer outside if else

once we break out of while, return true, there's cycle
"""

# For Two pointers or Tortoise Hare O(n) for time complexity and O(1) for space complexity
"""
initialize two pointers at head
while pointerB and pointerA are valid
increase the traversal by 1 for A and 2 for B
inside loop, check if both A and B are equal: return True

else after loop is invalid, return False
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

        # We might need to handle this if we don't have a value given.
        # if head == None: return False
        
        while pointerB and pointerA and pointerB.next:  # Included the pointerB.next as loop codition to fix the error 
            # popping up about pointerB.next.next below.
            pointerA = pointerA.next
            pointerB = pointerB.next.next
        
            if pointerB == pointerA: return True
        return False

