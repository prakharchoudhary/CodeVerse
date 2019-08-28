import random

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

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            self.last = self.head
        else:
            newNode = Node(val)
            self.last.next = newNode
            self.last = newNode
    
    def push(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode

    def printlist(self):
        curr = self.head
        elems = []
        while curr is not None:
            elems.append(curr.val)
            curr = curr.next
        print(' -> '.join(list(map(str, elems))))

def partition(head, seperator):
    newList = LinkedList()
    ptr = head
    while ptr is not None:
        if ptr.val < seperator:
            newList.push(ptr.val)
        else:
            newList.append(ptr.val)
        temp = ptr
        ptr = ptr.next
        del temp
    return newList

if __name__ == '__main__':
    llist = LinkedList()
    for i in range(10):
        newelem = random.randint(0, 9)
        llist.append(newelem)
    print("Old list:")
    llist.printlist()
    newList = partition(llist.head, 5)
    print("New list:")
    newList.printlist()
