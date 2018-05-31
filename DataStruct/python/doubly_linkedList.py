import sys


class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            if sys.version_info > (2, 7):
                print(temp.data, end=' ')
            else:
                print(temp.data,)
            temp = temp.right
        print('\n')

    # function to insert a new node
    def insert(self, new_data, pos=None, afteritem=None):
        new_node = Node(new_data)
        if afteritem is None:
            if pos is None:
                if self.head is None:
                    self.head = new_node
                    return

                temp = self.head
                print(temp.data)
                while(temp.right):
                    temp = temp.right
                temp.right = new_node
                new_node.left = temp
                return

            if pos >= 1:
                p = 0
                temp = self.head
                while p != pos - 1:
                    p += 1
                    temp = temp.right
                new_node.left = temp
                new_node.right = temp.right
                temp.right = new_node
                new_node.right.left = new_node
                return
        else:
            temp = self.head
            while(temp.right and temp.data != afteritem):
                temp = temp.right
            if temp.data != afteritem:
                print("No such item exists in the list.")
                return
            new_node.left = temp
            new_node.right = temp.right
            temp.right = new_node
            new_node.right.left = new_node
            return

    def delete(self, item=None):
        if item is None:
            # Delete from the beginning
            temp = self.head
            self.head = self.head.right
            self.head.left = None
            del temp

        else:
            temp = self.head
            while(temp.right and temp.data != item):
                temp = temp.right
            if temp.data != item:
                print("No such item exists in the list.")
                return
            temp.left.right = temp.right
            temp.right.left = temp.left
            del temp
            return
