#include <stdio.h>

struct stack
{
	int data;
	struct stack* next;
};

struct stack* newNode(int data){
	struct stack* new = (struct stack*)malloc(sizeof(struct stack));
	new->data = data;
	new->next = NULL;
	return new;
}

int isEmpty(struct stack *top)
{
	return !top;
}

void push(struct stack** top, int data)
{
	struct stack* new = newNode(data);
	new->next = *top;
	*top = new;
}

void pop(struct stack** top)
{
	if(!isEmpty(*top)){
		struct stack* temp = *top;
		*top = (*top)->next;
		int pop = temp->data;
		free(temp);

		printf("The popped number is %d\n", pop);
		return;
	}
	printf("The stack is empty.\n");
}

void stacktop(struct stack *top){
	if(!isEmpty(top)){
		printf("The topmost element is: %d\n", top->data);return;
	}
	printf("Stack is empty!\n");
}

void display(struct stack* root)
{
	if(root==NULL){
		printf("\nStack is Empty!!!\n");
	}
	else{
		struct stack* temp = root;
		while(temp->next!=NULL){
			printf("%d  ", temp->data);
			temp = temp->next;
		}
		printf("%d\n", temp->data);
	}
}

void main(){
	int n, ch, val;
	struct stack *root = NULL;
	printf("Enter your choice:\n1. To push a number.\n2. To pop from the stack.\n3. To display the stack.\n4. To find the topmost element.\n");
	do{
		printf("Enter your choice: ");
		scanf("%d", &ch);
		switch(ch)
		{
			case 1:
				printf("Enter the element to be pushed: ");
				scanf("%d", &n);
				push(&root, n);
				break;
			case 2:
				pop(&root);
				break;
			case 3:
				display(root);
				break;
			case 4:
				stacktop(root);
				break;
		}
	}while(ch==1||ch==2||ch==3||ch==4);
}