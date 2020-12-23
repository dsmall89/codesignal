def invertBinaryTree(tree):
    if tree:
        left = tree.left
        right = tree.right
        #invert children node from    1    to    1
                                #    /  \       /  \
                                #    2   3      3   2
                                                        
        tree.left =right
        tree.right = left
        #Recursively traverse tree switching node values.
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
   

class BinaryTree(object):
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right = None   