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
we could use a flag to store our truthy state
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # while head.next:
        #     print(head)
        #     head = head.next

        # if head.next != None: 
        #     return True
        # else: return False
        hashmap = {}

        if head == None: return False

        while head.next not in hashmap:
            hashmap[head.next] = head.val
            if head.next == None: 
                return False
            head = head.next
        
        return True
