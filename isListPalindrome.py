#Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


'''
Algorithm:  O(n) time, 0(n) space
1. For every element in the LL, fill it into a Array 
2. After the array is filled, reverse one the array
3. Compare the reversed array to original array for equality
Note: Cost about n space and we have to reverse one array
'''
def isListPalindrome(head):
    if not head:
            return True
        
    arr = []
    while head:
        arr.append(head.value)
        head = head.next
    
    return arr == arr[::-1]
    
head_True = [0, 1, 0]
head_False = [1, 2, 2, 3]
isListPalindrome(head_True )
