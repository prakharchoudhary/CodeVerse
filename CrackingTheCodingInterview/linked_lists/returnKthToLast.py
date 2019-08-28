class Node:
    '''
    Node class for a linked list.
    '''
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
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

def kthToLast(head, k):
    marker = aheadPtr = head
    count = 0
    while aheadPtr is not None:
        aheadPtr = aheadPtr.next
        if count <= k:
            count += 1
        else:
            marker = marker.next
    return marker.val

if __name__ == '__main__':
    llist = LinkedList()
    for i in range(26):
        llist.append(chr(i+97))
    head = llist.head
    print(kthToLast(head, 3))
    print(kthToLast(head, 0))
    print(kthToLast(head, 26))
