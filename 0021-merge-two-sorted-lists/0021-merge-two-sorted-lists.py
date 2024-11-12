# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # I don't know how but my code works after so many hours of trial and error!!!
    # Hahahaha

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
            # return current
           
        if head1 == None and head2:
            head1 = head2
            return head1
        elif head1 == None and head2 == None:
            return None
        if head1 and head1.next == None: 
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
