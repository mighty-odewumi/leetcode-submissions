# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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
           
            
        if head1 == None and head2 and node == None:
            head1 = head2
            return head1
        elif head1 == None and head2 == None and node == None:
            return None
        if head1 and head1.next == None and node == None: 
            head1.next = head2
            node = head1
            sortLinkedList(node)
            return node

        count = 0

        # while head1.next:
        #     count += 1
        #     head1 = head1.next
        # print("count", count)

        # # if count == 1:
        # if head1.next == None:
        #     head1.next = head2

        while head1.next:
            node = head1
            break

        print("Head1", head1)
        print("Node", node)
        if node:
            # node.next = head1.next
            print("Huh", node)
            while node.next:
                print(node)
                node = node.next
            node.next = head2
        print("New node", node)
        print(head1)

        print(head1)
        sortLinkedList(head1)
        print(head1)
        return head1
