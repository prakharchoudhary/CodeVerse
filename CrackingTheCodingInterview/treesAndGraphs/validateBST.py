INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def validateBST(root):
    return isBST(root, INT_MIN, INT_MAX)

def isBST(node, mini, maxx):
    if node is None: 
        return True

    if node.val < mini or node.val > maxx: 
        return False

    return (isBST(node.left, mini, node.val-1) and
          isBST(node.right, node.val+1, maxx)) 

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
        left=Node(3, 
                left=Node(1), 
                right=Node(4)
                ), 
        right=Node(8, 
                left=Node(6),  
                right=Node(9)
                )
        )
    tree3 = Node(10, 
        left=Node(5, 
                ), 
        right=Node(15, 
                left=Node(6),  
                right=Node(20)
                )
        )

    print(validateBST(tree1)) # Required output -> False
    print(validateBST(tree2)) # Required output -> True
    print(validateBST(tree3)) # Required output -> False