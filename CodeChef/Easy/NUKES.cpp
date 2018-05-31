#include <iostream>

using namespace std;

int check(int C[], int i, int N)
{
	if(C[i] < N)
	{
		C[i]++;
		return 0;
	}
	C[i] = 0;
	if(C[i+1]<N){
		check(C, i+1, N);
	}
}

int main()
{
	long int A, i;
	int N, K;
	cin>>A>>N>>K;
	int chambers[100] = {0};
	for(i=0; i<A; i++)
	{
		check(chambers, 0, N);
	}
	for(int j=0; j<K; j++)
	{
		cout<<chambers[j]<<" ";
	}
	cout<<endl;
	return 0;
}