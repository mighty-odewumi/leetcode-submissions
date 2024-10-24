# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0

        if current.next == None:
            return current

        while current:
            count += 1
            current = current.next
        
        mid = (count // 2) + 1
        newCount = 1
        current = head
        while newCount < count:
            newCount += 1
            current = current.next
            # print("[", end="")
            if newCount >= mid:
                # if (current.next != None):
                print(current.val, end=",")
                return current
