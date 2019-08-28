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

def checkPalindrome(head):
    '''
    Check if given list is a palindrome.
    '''
    slowptr = fastptr = head
    isPalindrome = True
    stack = [slowptr.val]
    while fastptr.next and fastptr.next.next:
        slowptr = slowptr.next
        fastptr = fastptr.next.next
        stack.append(slowptr.val)
    if fastptr.next:
        # list is of even length
        slowptr = slowptr.next
    while slowptr is not None:
        if slowptr.val == stack[-1]:
            stack.pop()
            slowptr = slowptr.next
        else:
            isPalindrome = False
            break
    return isPalindrome

if __name__ == "__main__":
    llist = LinkedList.extend("abcba")
    print(checkPalindrome(llist.head))        