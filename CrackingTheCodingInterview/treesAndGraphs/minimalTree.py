import math

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)
    
def minimalTree(arr):
    '''
    Return root of BST formed from given sorted array of unique
    characters.
    '''
    arrlen = len(arr)
    if arrlen == 0:
        return None
    elif arrlen == 1:
        return Node(arr[0])
    else:
        mid = math.ceil(arrlen/2) - 1
        root = Node(arr[mid])
        root.left = minimalTree(arr[:mid])
        root.right = minimalTree(arr[mid+1:])
        return root

def printTree(root):
    '''
    Print tree in an aesthetic format.
    '''
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level

if __name__ == '__main__':
    # arr = [1,2,3,4,5,6,7,8]
    arr = [2,9,18,23,54,77,1116]
    tree = minimalTree(arr)
    printTree(tree)