# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) Time complexity solution from NeetCode
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2: 
            tail.next = list2
            
        return dummy.next

        
        # My initial implementation!
        # I don't know how but my code works after so many hours of trial and error!!!
        # Hahahaha
        # O(n**2) Time Complexity and O(1) space complexity! :(
        # Off to the Discussions. 
        """
        head1 = list1
        head2 = list2
        node = None
        
        def sortLinkedList(head):
            current = head
            index = ListNode(None)

            if head is None: return

            while current:
                index = current.next

                while index:
                    if current.val > index.val:
                        current.val, index.val = index.val, current.val
                    index = index.next
                current = current.next
           
        if head1 == None and head2:
            head1 = head2
            return head1
        elif head1 == None and head2 == None:
            return None
        elif head1 and head1.next == None: 
            head1.next = head2
            node = head1
            sortLinkedList(node)
            return node

        while head1.next:
            node = head1
            break

        if node:
            while node.next:
                node = node.next
            node.next = head2
        
        sortLinkedList(head1)
        return head1
        """
