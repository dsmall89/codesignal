'''
      5
     / \
   3    7 
  /\    /\
 2  4   6 8       

 Given 5--> 6
 Given 6--> 7
 Given 8 --> None
 Time O(n)
 Space O(n) because we trav and store value

 BCR: 
 Time: 0(logn)
 Space: 0(logn) or 0(1)

 Cases :
 1) Search node has right child -- get smallest element in right subtree

 2) If node has no children -> return next largest number (init to None)
'''

def get_smallest(node):
    if not node.left:
        return node.val
    return get_smallest(node.left)

def find_node(node, num):
    if node.val == num:
        return node
     elif node.val < num:
        return find_node(node.right, num)
    else node.val > num:
        return find_node(node.left, num)


def binaryTreeTraversal(node, next_largest):
    if not node:
        return next_largest
    elif node.right:
    else: 
        return 
