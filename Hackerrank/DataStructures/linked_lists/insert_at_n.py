"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    count = 0
    node = Node()
    node.data=data
    
    truehead = head
    if head == None:
        return head

    if position==0:
        node.next = head
        return node
    else:
        while(count<position-1 and head.next!=None):
            head = head.next
            count += 1

    nodeAtPosition = Node()
    nodeAtPosition = head.next;
    head.next = node;
    head = head.next;
    head.next = nodeAtPosition
    
    return truehead