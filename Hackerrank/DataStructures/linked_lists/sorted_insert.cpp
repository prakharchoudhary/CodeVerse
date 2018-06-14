//-------------------------------------------------------------------------
//---------------------- Submission ---------------------------------------
//-------------------------------------------------------------------------

DoublyLinkedListNode* sortedInsert(DoublyLinkedListNode* head, int data) {
    // DoublyLinkedListNode* temp = head;
    DoublyLinkedListNode* newnode = new DoublyLinkedListNode(data);
    if(head==NULL)
        return newnode;
    if(head->data <= data){
        head->next = sortedInsert(head->next, data);
        head->next->prev = head;
    }
    else{
        newnode->data = data;
        newnode->next = head;
        newnode->prev = head->prev;
        head->prev = newnode;
        head = newnode;        
    }
    return head;
}

//-------------------------------------------------------------------------
//-------------------------------------------------------------------------
