/*
  Insert Node at the begining of a linked list
  Initially head pointer argument could be NULL for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
return back the pointer to the head of the linked list in the below method.
*/
Node* Insert(Node *head,int data)
{
  // Complete this method
    Node* node = new Node();
    node->data = data;
    node->next = NULL;
    
    if (head==NULL){
        head = node;
        return(head);
    }
    
    node->next = head;
    head = node;
    return(head);
}