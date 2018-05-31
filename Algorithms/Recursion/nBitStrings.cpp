/*
Program to generate all the strings of n-bits.
*/

#include<iostream>
using namespace std;

char A[1000];
void nBitStrings(int);

int main()
{
	int N;
	cout<<"Enter the string size: ";
	cin>>N;
	nBitStrings(N); 
}

void nBitStrings(int n)
{
	if(n<1){
		cout<<A<<endl;
	}
	else{
		A[n-1] = '0';
		nBitStrings(n-1);
		A[n-1] = '1';
		nBitStrings(n-1);
	}
}