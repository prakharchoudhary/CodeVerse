class Node:
    '''
    Node class for a linked list.
    '''
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    '''
    Linked List class.
    '''
    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def append(self, val: (int, str)):
        self.count += 1
        if not self.head:
            self.head = Node(val)
            self.last = self.head
        else:
            newNode = Node(val)
            self.last.next = newNode
            self.last = newNode
    
    @classmethod
    def extend(cls, values: list):
        newList = cls()
        for v in values:
            newList.append(v)
        return newList

    def printlist(self):
        curr = self.head    
        elems = []
        while curr is not None:
            elems.append(curr.val)
            curr = curr.next
        print(' -> '.join(list(map(str, elems))))

def intersection(l1, l2):
    '''
    Find the intersection node.
    '''
    len_diff = abs(l1.count - l2.count)
    h1, h2 = l1.head, l2.head
    count = 0
    intersection = None
    if not len_diff:
        if l1.count > l2.count:
            while count < len_diff:
                h1 = h1.next
                count += 1
        else:
            while count < len_diff:
                h2 = h2.next
                count +=1
    while h1 and h2:
        if h1.val == h2.val:
            if h1.next == h2.next:
                intersection = h1
                break
        h1 = h1.next
        h2 = h2.next
    return intersection