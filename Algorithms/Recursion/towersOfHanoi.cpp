/*
Solution to the famous Towers of Hanoi Problem using Recursion.
*/

#include <iostream>

using namespace std;

void TowersOfHanoi(int n, char frompeg, char topeg, char auxpeg)
{
	// Base case: if only one disk, make move and return.
	if(n==1)
	{
		cout<<"Move disk 1 from "<<frompeg<<" to "<<topeg<<endl;
		return;
	}

	// Move the top n-1 disks from source to auxiliary peg
	TowersOfHanoi(n-1, frompeg, auxpeg, topeg);

	// Move the nth disk from source to destination peg
	cout<<"Move disk "<<n<<" from "<<frompeg<<" to "<<topeg<<endl;

	// Move the n-1 disks back auxiliary to destination peg
	TowersOfHanoi(n-1, auxpeg, topeg, frompeg);
}

int main()
{
	int n;
	char A='A', B='B', C='C';
	cout<<"Enter the number of disks on source A: ";
	cin>>n;
	TowersOfHanoi(n, A, B, C);
	return 0;
}