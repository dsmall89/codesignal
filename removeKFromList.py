# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(head, val):
        while head and head.value==val:
            head = head.next
        curr = head
        while curr:
            if curr.next and curr.next.value == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head