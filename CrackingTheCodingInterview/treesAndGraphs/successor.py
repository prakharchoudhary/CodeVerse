class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __str__(self):
        return str(self.val)

def leftMost(node):
    if node.left is None:
        return node
    return leftMost(node.left)

def successor(node):
    '''
    Returns the in-order successor of the node.
    '''
    if node is None:
        return None

    if node.right is None:
        next_node = node.parent
        while next_node and node.val > next_node.val:
            next_node = next_node.parent
        return next_node

    return leftMost(node.right)

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

    print(successor(tree)) # => 6
    print(successor(tree.left.left)) # => 3
    print(successor(tree.left.right)) # => 5
    print(successor(tree.right.left.left)) # => 7
    print(successor(tree.right.right)) # => 12
    print(successor(tree.right.right.right)) # => None

