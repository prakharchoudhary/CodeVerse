// A simple C program for traversal of a linked list
#include<stdio.h>
#include<stdlib.h>
 
struct node 
{
  int data;
  struct node *next;
};  
 
// This function prints contents of linked list starting from 
// the given node
void printList(struct node *n)
{
  while (n != NULL)
  {
     printf(" %d ", n->data);
     n = n->next;
  }
}

void push(struct node** head_ref, int new_data){
  //allocate a new node
  struct node* new_node = (struct node*)malloc(sizeof(struct node));
  //assign the data
  new_node->data = new_data;
  //make next of new node as head
  new_node->next = (*head_ref);
  //move the head to point to the new node
  (*head_ref) = new_node;
}

void insertAfter(struct node* prev_node, int new_data)
{
    if (prev_node == NULL)
    {
      printf("the given previous node cannot be NULL");
      return;
    }
 
    struct node* new_node =(struct node*) malloc(sizeof(struct node));
 
    new_node->data  = new_data;
 
    new_node->next = prev_node->next;
 
    prev_node->next = new_node;
}

void append(struct node** head_ref, int new_data)
{
    struct node* new_node = (struct node*) malloc(sizeof(struct node));
 
    struct node *last = *head_ref;  /* used in step 5*/

    new_node->data  = new_data;

    new_node->next = NULL;
 
    if (*head_ref == NULL)
    {
       *head_ref = new_node;
       return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = new_node;
    return;
}
 
int main()
{
  char c;
  int i;
  struct node* head = NULL;
  struct node* second = NULL;
  struct node* third = NULL;
   
  // allocate 3 nodes in the heap  
  head  = (struct node*)malloc(sizeof(struct node)); 
  second = (struct node*)malloc(sizeof(struct node));
  third  = (struct node*)malloc(sizeof(struct node));
  
  head->data = 1; //assign data in first node
  head->next = second; // Link first node with second   
  
  second->data = 2; //assign data to second node
  second->next = third;  
  
  third->data = 3; //assign data to third node
  third->next = NULL;
  printList(head);
  while(1)
  { 
    printf("\nEnter p to push, i to insert after, a to append, q to quit: ");
    scanf("%c", &c);
    if(c != 'q'){
      if(c == 'p')
      {
        printf("Enter the number to push: ");
        scanf("%d", &i);
        push(&head, i);
      }
      else if(c == 'i'){
        printf("Enter the number to insert after the current head: ");
        scanf("%d", &i);
        insertAfter(head->next, i);
      }
      else if(c == 'i'){
        printf("Enter the number to append: ");
        scanf("%d", &i);
        append(&head, i);
      }
      printList(head);
    }
    else if(c == 'q'){
      break;
    }
  }
  return 0;
}
