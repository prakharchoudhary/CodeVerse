class Node:
	def __init__(self, data):
		self.data = data #assign data
		self.next = None #initialize next as null

class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next

	#function to insert a new node at the beginning 
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	#function to add a new node after the given prev_node
	def insertAfter(self, prev_node, new_data):
		if prev_node is None:
			print "The given previous node must be in LinkedList."
			return

		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while(last.next):
			last = last.next

		last.next = new_node


if __name__=='__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second;
	second.next = third;

	llist.push(6)
	llist.insertAfter(llist.head.next, 9)
	llist.insertAfter(llist.head.next, 7)
	llist.append(5)

	llist.printList()