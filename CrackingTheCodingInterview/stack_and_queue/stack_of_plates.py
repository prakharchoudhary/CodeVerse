class Node:
    '''
    Node class for stack.
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

    def push(self, val):
        '''
        Push new value to top of stack.
        '''
        print("Pushing to the stack:", val)
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
            print('Popped out:', val)
            return val

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

class SetOfStacks:
    '''
    Class for collection of stack objects.
    '''
    def __init__(self, threshold=3):
        self.stacks = []
        self.topIdx = None
        self.threshold = threshold

    def push(self, val):
        if len(self.stacks) == 0 and self.topIdx == None:
            self.stacks.append(Stack())
            self.topIdx = 0
            self.stacks[0].push(val)
        elif self.stacks[self.topIdx].count == self.threshold:
            self.stacks.append(Stack())
            self.topIdx += 1
            self.stacks[self.topIdx].push(val)
        else:
            self.stacks[self.topIdx].push(val)
    
    def pop(self, idx=None):
        try:
            if len(self.stacks) == 0:
                print("Set of stacks empty")
                return
            if idx is None:
                idx = self.topIdx
            if self.stacks[idx].count == 1:
                self.stacks[idx].pop()
                del self.stacks[idx]
                self.topIdx -= 1
            else:
                self.stacks[idx].pop()

        except IndexError:
            print("Index out of reach.")
            return

    def printSetOfStacks(self):
        for sid, stack in enumerate(self.stacks):
            print("Printing stack", sid + 1)
            stack.printStack()

if __name__ == '__main__':
    setofstacks = SetOfStacks()
    for i in range(10):
        setofstacks.push(i)
    setofstacks.printSetOfStacks()
    setofstacks.pop(3)
    setofstacks.pop(2)
    setofstacks.pop(1)
    setofstacks.pop(4)
    setofstacks.pop()
    setofstacks.pop()
    setofstacks.printSetOfStacks()
