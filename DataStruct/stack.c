#include <stdio.h>
#include <string.h>
#define STACKSIZE 100

struct stack {
	int top;
	int items[STACKSIZE];	
};

int empty(struct stack *s)
{
	if(s->top == -1)
		return 1;
	return 0;	
}

int pop(struct stack *s){
	if(!empty(s)){
		return (s->items[s->top--]);
	}
	else
		printf("Underflow\n");
		return;	
}

int stackfull(struct stack *s){
	if(s->top == STACKSIZE - 1)
		return 1;
	return 0;	
}

void push(struct stack *s, int x){
	if(!stackfull(s)){
		s->items[++(s->top)] = x;
		return;
	}
	else{
		printf("stack overflow\n");
		return;
	}
}

void printStack(struct stack *s){
	int i;
	for (i=s->top; i>=0; i--){
		printf("%d ", s->items[i]);
	}
	printf("\n");
}

struct stack s;

int main(){
	s.top = -1;
	push(&s, 1);
	printStack(&s);
	push(&s, 5);
	printStack(&s);
	push(&s, 4);
	push(&s, 6);
	push(&s, 19);
	printStack(&s);
	push(&s, 18);
	printStack(&s);
	pop(&s);
	printStack(&s);
	return 0;
}