/*
Stack Min: How would you design a stack which, in addition to push 
and pop, has a function min which returns the minimum element? 
Push, pop and min should all operate in 0(1) time.
*/
#include<iostream>
#include<cstdlib>
#include<ctime>
#include<climits>
#include <vector>

using namespace std;

class Stack{

	int StackCapacity;
	vector<int> values;
	int min = INT_MAX;
	int indexOfTop = 0;

public:
	Stack(int stackSize){
		StackCapacity = stackSize;
		values.resize(stackSize);
	}

	/*push element in stack*/
	void push(int val){
		if(isFull())
			throw "Stack Overflow";
		values[indexOfTop] = val;
		indexOfTop++;
		min = val<min?val:min;
	}

	/*pop the top element*/
	int pop(){
		if(isEmpty())
			throw "Stack is Empty";
		int popVal = values[indexOfTop];
		values[indexOfTop] = 0;
		indexOfTop--;
		return popVal;
	}

	/*check if stack is full*/
	bool isFull(){
		return indexOfTop == StackCapacity;
	}

	/*check if stack is empty*/
	bool isEmpty(){
		return indexOfTop<=0;
	}

	int peek(){
		return values[indexOfTop];
	}

	int stackMin(){
		cout<<"The min of stack is "<<min<<endl;
	}

	/*print the stack*/
	void printStack(){
		int topIdx = indexOfTop;
		while(--topIdx){
			cout<<values[topIdx]<<" ";
		}
		cout<<endl;
	}
};

int main(){
	srand((int) time(nullptr));
	Stack stack(10);
	for(int i=0; i<10; i++){
		stack.push(rand() % 10);
	}
	stack.printStack();
	stack.stackMin();
	return 1;
}