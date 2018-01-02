#include<stdio.h>
#include<stdlib.h>

struct node 
{
  int data;
  struct node *next;
};  

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

void printlist(struct node* n){
	while(n!=NULL){
		printf(" %d ", n->data);
		n = n->next;
	}
}


int main(){
	int i;
	char ch;
	struct node* head = NULL;
	head = (struct node*)malloc(sizeof(struct node));
	head->data = 0;
	head->next = NULL;
	while(1){
		printf("\nDo you wish to push some data in the list?[y/n]: ");
		scanf("%c", &ch);
		if(ch=='y'){
			printf("Enter the new data: ");
			scanf("%d", &i);
			push(&head, i);
			printf("\n");
			printlist(head);
		}else{
			printf("\nThe final list is as below:\n");
			printlist(head);
			break;	
		} 
	}
}

