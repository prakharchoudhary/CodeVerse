import sys


class Node:

    def __init__(self, data=None):
        self.data = data  # assign data
        self.next = None  # initialize next as null


class Stack:

    def __init__(self):
        self.top = None

    def getTop(self):
        if not self.top:
            print('Top is Null')
            return
        print(self.top.data)

    def isStackEmpty(self):
        if not self.top:
            return True
        return False

    def push(self, item, verbose=False):
        new_Node = Node(item)
        if self.top is None:
            self.top = new_Node
        else:
            new_Node.next = self.top
            self.top = new_Node
        if verbose:
            self.printStack()
        return

    def pop(self, verbose=False):
        if not self.isStackEmpty():
            temp = Node()
            temp = self.top
            self.top = self.top.next
            del temp
            if verbose:
                self.printStack()
            return
        print('Stack is Empty!')

    def getSize(self):
        temp = Node()
        temp = self.top
        count = 0
        if not self.isStackEmpty():
            while temp:
                count += 1
                temp = temp.next
            return count
        print("Stack is Empty!")

    def printStack(self):
        temp = Node()
        temp = self.top
        if not self.isStackEmpty():
            while temp:
                print(temp.data, end=' ')
                temp = temp.next
            print('\n')
        else:
            print("Stack is Empty!")

if __name__ == '__main__':
    stack = Stack()
    stack.push(5, verbose=True)
    stack.push(6, verbose=True)
    stack.push(7, verbose=True)
    print("Size of the stack is %d" % stack.getSize())
    stack.pop(verbose=True)
    stack.pop(verbose=True)
    print("Size of the stack is %d" % stack.getSize())
