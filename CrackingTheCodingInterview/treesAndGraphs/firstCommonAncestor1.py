'''
Allows the assumption that each node has a link to its parent.
'''
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

def getDepth(root):
    if root is None:
        return 0
    return 1 + getDepth(root.parent)

def firstCommonAncestor(node1, node2):
    '''
    My approach: Find depths of both nodes, traverse deeper node until diff is 0
    and then traverse both together until they reach a common point or the root.
    '''
    if node1 and node2:
        h1 = getDepth(node1)
        h2 = getDepth(node2)
        diff = abs(h1 - h2)
        while diff:
            if h1 > h2:
                node1 = node1.parent
            elif h1 < h2:
                node2 = node2.parent
            diff -= 1
        while node1 and node2:
            if node1.val == node2.val:
                return node1.val
            node1 = node1.parent
            node2 = node2.parent

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
    
    print(firstCommonAncestor(tree1.right.left.left, tree1.right.right)) # -> 2
    print(firstCommonAncestor(tree1.left, tree1.right.left.right)) # -> 5

    print(firstCommonAncestor(tree2, tree2.right.left.right)) # -> 5
    print(firstCommonAncestor(tree2.left, tree2.right.left.right)) # -> None
