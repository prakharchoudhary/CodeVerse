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

def removeDups(head):
    '''
    Removes duplicates in a Linked List.
    '''
    char_map = {}
    current = head
    prev = None
    while current is not None:
        if char_map.get(ord(current.val) - 97, None):
            if prev:
                prev.next = current.next
            temp = current
            del temp
        else:
            char_map[ord(current.val) - 97] = True
        prev = current
        current = current.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.append('a')
    llist.append('b')
    llist.append('c')
    llist.append('a')
    llist.append('d')
    llist.append('c')
    llist.printlist()
    removeDups(llist.head)
    llist.printlist()
    