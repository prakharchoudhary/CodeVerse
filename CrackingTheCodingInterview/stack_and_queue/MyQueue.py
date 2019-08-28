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

class MyQueue:
    '''
    Implementing queue using two stacks.
    '''
    def __init__(self):
        self.priStack = Stack()
        self.auxStack = Stack()
    
    def enqueue(self, val):
        if self.priStack.top == None:
            self.priStack.push(val)
        else:
            while self.priStack.top is not None:
                popVal = self.priStack.pop()
                self.auxStack.push(popVal)
            self.priStack.push(val)
            while self.auxStack.top is not None:
                popVal = self.auxStack.pop()
                self.priStack.push(popVal)
    
    def dequeue(self):
        if self.priStack.top is None:
            print("Queue is empty!")
            return 
        val = self.priStack.pop()
        return val
    
    def printQueue(self):
        if self.priStack.top is None:
            print("Can't print anything, Queue is empty.")
        head = self.priStack.top
        elems = []
        while head is not None:
            elems.append(head.val)
            head = head.next
        elems = list(map(str, elems))
        print(' -> '.join(elems))

if __name__ == '__main__':
    q = MyQueue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(1)
    q.printQueue()
    q.dequeue()
    q.dequeue()
    q.printQueue()    
    q.dequeue()
    q.dequeue()
    q.printQueue()    
    q.enqueue(4)
    q.enqueue(5)
    q.printQueue()    
