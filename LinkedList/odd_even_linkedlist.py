'''
odd_even_linkedlist

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
'''

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#     

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd = p1 = head
        even = p2 = head.next
        
        while p1.next and p2.next:
            p1.next = p2.next
            p1 = p1.next
            if p1.next:
                p2.next = p1.next
                p2 = p2.next
        p1.next = even
        p2.next = None
        
        return head