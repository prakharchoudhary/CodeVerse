import random

class Node:
    def __init__(self, val, left=None, right=None):
        '''
        Constructor for Node class.
        '''
        self.val = val
        self.left = left
        self.right = right
        self.size = 1

    def __str__(self):
        '''
        Print node values.
        '''
        return str(self.size)

    def insert(self, val):
        '''
        Insert a new node.
        '''
        if val <= self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        self.size += 1

    def getIthNode(self, i):
        '''
        Get ith node.
        '''
        leftSize = 0
        if self.left:
            leftSize = self.left.size
        if i < leftSize:
            return self.left.getIthNode(i)
        elif i == leftSize:
            return self
        else:
            return self.getIthNode(i - (leftSize + 1))

class Tree:
    def __init__(self):
        '''
        Constructor for Tree class.
        '''
        self.root = None

    @property
    def size(self):
        if self.root:
            return self.root.size
        return None

    def insert(self, val):
        '''
        Insert a new node in tree.
        '''
        if self.root == None:
            self.root = Node(val)
        else:
            self.root.insert(val)

    def randomNode(self):
        '''
        Spit out a random node.
        '''
        if self.root is None:
            return None
        r = random.randint(1, self.size)
        return self.root.getIthNode(r)
    
    def printTree(self):
        '''
        Print tree in an aesthetic format.
        '''
        current_level = [self.root]
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
    tree = Tree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(1)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    # Print a random node
    print(tree.randomNode())
        