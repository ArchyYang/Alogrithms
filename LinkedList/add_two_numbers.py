'''
Add Two Numbers

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def addTwoNumbers(self, l1, l2):    
	head = ListNode(0)
	cur = head
	carry = 0
	while l1 or l2:
	    sum = carry
	    carry = 0
	    if l1:
	        sum = sum + l1.val
	        l1 = l1.next
	    if l2:
	        sum = sum + l2.val
	        l2 = l2.next
	    if sum >= 10:
	        carry = 1
	    sum = sum % 10
	    cur.next = ListNode(sum)
	    cur = cur.next
	if carry != 0:
	    cur.next = ListNode(carry)
	    cur = cur.next
	return head.next