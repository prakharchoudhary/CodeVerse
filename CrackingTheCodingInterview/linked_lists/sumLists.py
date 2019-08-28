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

    def append(self, val: (int, str)):
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

def sumBackwardLists(h1, h2):
    placeVal = 1
    summ = 0
    rem = 0
    while True:
        if h1 is None and h2 is None:
            break
        elif h1 and h2:
            partialSum = h1.val + h2.val + rem
            if h1.next is None and h2.next is None:
                summ += partialSum * placeVal
                rem = 0
            else:
                summ += (partialSum % 10) * placeVal
                rem = partialSum // 10
            h1 = h1.next
            h2 = h2.next
        elif h1:
            partialSum = h1.val + rem
            if h1.next is None:
                summ += partialSum * placeVal
                rem = 0
            else:
                summ += (partialSum % 10) * placeVal
                rem = partialSum // 10
            h1 = h1.next
        elif h2:
            partialSum = h2.val + rem
            if h2.next is None:
                summ += partialSum * placeVal
                rem = 0
            else:
                summ += (partialSum % 10) * placeVal
                rem = partialSum // 10
            h2 = h2.next
        placeVal *= 10
    return summ

if __name__ == '__main__':
    # list1 = LinkedList.extend([7,1,6])
    # list2 = LinkedList.extend([5,9,2])
    list1 = LinkedList.extend([9,7,8])
    list2 = LinkedList.extend([6,8,5])
    list1.printlist()
    list2.printlist()
    total = sumBackwardLists(list1.head, list2.head)
    print("Sum is ", total)