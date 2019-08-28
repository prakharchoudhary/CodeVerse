import random

class Node:
    '''
    Node class for MyQueue.
    '''
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    '''
    Stack class.
    '''
    def __init__(self):
        self.top = None
        self.count = 0

    @property
    def seek(self):
        '''
        Returns the topmost element of stack.
        '''
        if self.top:
            return self.top.val
        return None

    def push(self, val):
        '''
        Push new value to top of stack.
        '''
        if self.top == None:
            self.top = Node(val)
        else:
            newNode = Node(val)
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
            return val

    @property
    def isEmpty(self):
        if self.count == 0:
            return True
        return False
    
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

def sortStack(stack):
    aux = Stack()
    if stack.seek is None:
        print("Empty Stack.")
        return
    else:
        while not stack.isEmpty:
            popval = stack.pop()
            if aux.seek is None or popval >= aux.seek:
                aux.push(popval)
            else:
                while aux.seek is not None and aux.seek > popval:
                    auxpop = aux.pop()
                    stack.push(auxpop)
                aux.push(popval)
    while aux.seek is not None:
        auxpop = aux.pop()
        stack.push(auxpop)

if __name__ == '__main__':
    stack = Stack()
    for _ in range(10):
        stack.push(random.randint(1,10))
    print("Original Stack:")
    stack.printStack()
    sortStack(stack)
    print("-"*(stack.count*3), end="\n")
    print("Sorted Stack:")
    stack.printStack()