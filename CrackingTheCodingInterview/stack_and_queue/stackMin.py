class Node:
    '''
    Node class for stack. Stores min of its substack under it.
    '''
    def __init__(self, val, next=None):
        self.val = val
        self.min = val
        self.next = next

class Stack:
    '''
    Stack class.
    '''
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, val):
        '''
        Push new value to top of stack.
        '''
        print("Pushing to the stack:", val)
        if self.top == None:
            self.top = Node(val)
            self.top.min = val
        else:
            newNode = Node(val)
            if self.top.min < val:
                newNode.min = self.top.min
            newNode.next = self.top
            self.top = newNode
        self.count += 1

    def pop(self):
        '''
        Remove and return value on top of the stack.
        '''
        if self.top == None:
            print("Stack empty!")
            return
        else:
            temp = self.top
            self.top = self.top.next
            val = temp.val
            del temp
            self.count -= 1
            print('Popped out:', val)
            return val
    
    def findMin(self):
        '''
        Return the minimum value in stack.
        '''
        print("Minimum of stack:", self.top.min)
        return self.top.min
    
    def printStack(self):
        '''
        Print values in the stack.
        '''
        head = self.top
        elems = []
        while head is not None:
            elems.append(head.val)
            head = head.next
        elems = list(map(str, elems))
        print(' -> '.join(elems))
    
if __name__ == '__main__':
    stack = Stack()
    stack.push(4)
    stack.push(5)
    stack.push(3)
    stack.push(9)
    stack.printStack()
    stack.pop()
    stack.pop()
    stack.printStack()
    stack.findMin()
    stack.push(1)
    stack.findMin()
    stack.printStack()
