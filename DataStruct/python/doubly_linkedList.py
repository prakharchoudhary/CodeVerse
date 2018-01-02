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
                print('\n')
            else:
                print(temp.data,)
            temp = temp.right

    # function to insert a new node
    def insert(self, new_data, pos=None, prev_node=None):
        new_node = Node(new_data)
        if pos is None:
            if self.head is None:
                self.head = new_node
                return

            temp = self.head
            while(temp):
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


if __name__ == '__main__':
    dllist = LinkedList()

    llist.push(6)
    llist.insertAfter(llist.head.next, 9)
    llist.insertAfter(llist.head.next, 7)
    llist.append(5)

    llist.printList()
