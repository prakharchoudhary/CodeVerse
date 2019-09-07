class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkSubtree(treelist1, treelist2):
    '''
    Check if treelist2 is a subset of treelist1.
    '''
    n = len(treelist2)
    return any(treelist2 == treelist1[i:i+n] for i in range(len(treelist1)-n+1))

def preOrderTraversal(root, nodeList):
    '''
    Return the pre-order traversal of a (sub)tree as an array.
    '''
    if root == None:
        nodeList.append("null")
        return
    # Traverse left
    preOrderTraversal(root.left, nodeList)
    # Traverse right
    preOrderTraversal(root.right, nodeList)
    # Get root
    nodeList.append(root.val)
    return nodeList

if __name__ == '__main__':
    tree = Node(5, 
        left=Node(3, 
                left=Node(1), 
                right=Node(4)
                ), 
        right=Node(9, 
                left=Node(7, left=Node(6)),  
                right=Node(11, left=Node(10), right=Node(12))
                )
        )
    treelist1 = preOrderTraversal(tree, [])
    treelist2 = preOrderTraversal(tree.left, [])
    treelist3 = preOrderTraversal(tree.right, [])
    print(checkSubtree(treelist1, treelist2)) # -> True
    print(checkSubtree(treelist2, treelist3)) # -> False