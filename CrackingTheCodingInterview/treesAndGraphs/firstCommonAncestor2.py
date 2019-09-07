'''
Nodes do not have any link to the parent.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def existsInSubtree(root, node):
    if root is None:
        return False
    if root.val == node.val:
        return True
    return existsInSubtree(root.left, node) or existsInSubtree(root.right, node)

def firstCommonAncestor(root, node1, node2):
    if not (node1 and node2):
        return None
    if not existsInSubtree(root, node1) or not existsInSubtree(root, node2):
        return None
    return ancestorHelper(root, node1, node2)

def ancestorHelper(root, node1, node2):
    if root is None or (root.val == node1.val or root.val == node2.val):
        return root
    in_left_1 = existsInSubtree(root.left, node1)
    in_left_2 = existsInSubtree(root.left, node2)
    if in_left_1 != in_left_2:
        return root
    if in_left_1:
        childroot = root.left
    else:
        childroot = root.right
    return ancestorHelper(childroot, node1, node2)

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
    
    print(firstCommonAncestor(tree1, tree1.right.left.left, tree1.right.right)) # -> 2
    print(firstCommonAncestor(tree1, tree1.left, tree1.right.left.right)) # -> 5 

    print(firstCommonAncestor(tree2, tree2, tree2.right.left.right)) # -> 5
    print(firstCommonAncestor(tree2, tree2.left, tree2.right.left.right)) # -> None