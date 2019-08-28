// Three in One: Describe how you could use a single array to implement 
// three stacks.

#include<iostream>
#include<cstdlib>
#include<ctime>
#include<vector>

using namespace std;

class FixedMultiStack
{
	int numOfStacks = 3;
	int stackCapacity;
	vector<int>values;
	vector<int>sizes;

public:
	FixedMultiStack(int stackSize)
	{
		stackCapacity = stackSize;
		values.resize(stackSize * numOfStacks);
		sizes.resize(numOfStacks);
	}

	/*push element in stack*/
	void push(int stackNum, int val){
		if(isFull(stackNum))
			throw "Stack Overflow";
		else{
			/*increment stack pointer and update top value*/
			sizes[stackNum]++;
			values[indexOfTop(stackNum)] = val;
		}
	}

	/*pop element from stack*/
	int pop(int stackNum){
		if(isEmpty(stackNum))
			throw "Stack Overflow";
		else{
			/* decrement stack pointer and return previously top value*/
			int topIdx = indexOfTop(stackNum);
			int val = values[topIdx];
			values[topIdx] = 0;
			sizes[stackNum]--;
			return val;
		}
	}

	/*check if stack is empty*/
	bool isEmpty(int stackNum){
		return sizes[stackNum] == 0;
	}

	/*check if stack is full*/
	bool isFull(int stackNum){
		return sizes[stackNum] == stackCapacity;
	}

	/*return top element*/
	int peek(int stackNum){
		if(isEmpty(stackNum))
			throw "Stack Empty";
		else{
			return values[indexOfTop(stackNum)];
		}
	}

	/*return index of the top of stack*/
	int indexOfTop(int stackNum){
		int offset = stackNum * stackCapacity;
		int size = sizes[stackNum];
		return offset + size - 1;
	}

	int printStack(int stackNum){
		int index = indexOfTop(stackNum);
		int sizeOfStack = sizes[stackNum];
		while(sizeOfStack){
			cout<<values[index]<<" ";
			sizeOfStack--;
			index--;
		}
		cout<<endl;
	}
};

int main(){
	srand((int) time(nullptr));
	FixedMultiStack multiStack(5);
	for(int i=0; i<10; i++){
		multiStack.push(rand() % 3, rand() % 10);
	}
	multiStack.printStack(0);
	multiStack.printStack(1);
	multiStack.printStack(2);

	return 1;
}