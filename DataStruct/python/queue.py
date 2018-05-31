import sys


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    # FIFO mannerism

    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, data):
        new_node = Node(data)
        if self.front == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        return

    def dequeue(self):
        if not self.isEmpty():
            temp = self.front
            self.front = self.front.next
            print(temp.data)
            del temp
            if self.rear and not self.rear:
                self.rear = None
            return
        print("Empty Queue")

    def isEmpty(self):
        if self.front == self.rear and self.front == None:
            return True
        return False

    def printFront(self):
        print(self.front.data)

    def printRear(self):
        print(self.rear.data)

    def printQueue(self):
        temp = self.front
        if not self.isEmpty():
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
        else:
            print("Queue is empty!")
