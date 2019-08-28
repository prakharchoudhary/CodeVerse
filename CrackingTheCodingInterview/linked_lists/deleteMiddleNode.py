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

    def append(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            newNode = Node(val)
            curr.next = newNode
    
    def printlist(self):
        curr = self.head
        elems = []
        while curr is not None:
            elems.append(curr.val)
            curr = curr.next
        print(' -> '.join(elems))

def deleteMiddleNode(head):
    fastPtr = slowPtr = head
    prev = None
    while fastPtr.next and fastPtr.next.next:
        prev = slowPtr
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
    if prev:
        prev = slowPtr.next
    print(slowPtr.val)
    del slowPtr

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(9):
        llist.append(chr(i+97))
    llist.printlist()
    deleteMiddleNode(llist.head)
    llist.printlist()