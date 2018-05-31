/*
Check is a given array is sorted, using Recursion
*/

#include<iostream>

using namespace std;

int isArraySorted(int*, int);

int main()
{
	int A[5] = {1,32,3,6,9};
	int B[6] = {10, 20, 30, 40, 50, 60};
	int C[6] = {6,5,4,3,2,1};

	cout<<"A is sorted: "<<(isArraySorted(A, 5)?"True":"False")<<endl;
	cout<<"B is sorted: "<<(isArraySorted(B, 6)?"True":"False")<<endl;
	cout<<"C is sorted: "<<(isArraySorted(C, 6)?"True":"False")<<endl;
	return 0;
}

/* Checks only for ascending order */
int isArraySorted(int A[], int n)
{
	if(n==1)
		return 1;
	return (A[n-1] < A[n-2])?0:isArraySorted(A, n-1);
}