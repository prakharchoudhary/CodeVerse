class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

# def getHeight(root):
#     if root is None:
#         return 0
#     return 1 + max(getHeight(root.left), getHeight(root.right))

# def isBalanced(root):
#     if root is None:
#         return True
#     lheight = getHeight(root.left)
#     rheight = getHeight(root.right)
#     print(root.val, lheight, rheight)

#     if (abs(lheight - rheight) <= 1) and isBalanced(root.left) is True\
#     and isBalanced(root.right) is True: 
#         return True
#     return False

################ Optimized Version #######################
'''
Store height in the same recursive call.
'''
class Height:
    def __init__(self):
        self.height = 0

def isBalanced(root, h): 
    lheight = Height() 
    rheight = Height() 

    if root is None: 
        return True

    l = isBalanced(root.left, lheight) 
    r = isBalanced(root.right, rheight) 

    h.height = max(lheight.height, rheight.height) + 1
  
    if abs(lheight.height - rheight.height) <= 1: 
        return l and r 

    return False


if __name__ == '__main__':
    tree1 = Node(5, 
        left=Node(3, 
                left=Node(1), 
                right=Node(8)
                ), 
        right=Node(2, 
                left=Node(4, 
                    left=Node(6), right=Node(9)), 
                right=Node(7)
                )
        )
    tree2 = Node(5,
        right=Node(2, 
                left=Node(4, 
                    left=Node(6), right=Node(9)), 
                right=Node(7)
                )
        )
    print(isBalanced(tree1, Height())) # Required output -> True
    print(isBalanced(tree2, Height())) # Required output -> False