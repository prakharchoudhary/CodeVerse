//usng counting sort
#include <iostream>
#define SIZE 100000
using namespace std;

int main()
{
	int n, i=0, arr[SIZE], index[SIZE], p[SIZE], val, max;

	cin>>n;
	while(i<n){
		cin>>arr[i];
		++i;
	}

	max = arr[0];
	for(i=0; i<n; ++i)
	{
		if (arr[i]>max)		//finding the maximum element in an array
			max=arr[i];
	}

	for(i=0; i<n; ++i)
	{
		val = arr[i];		//loop to add the number of instances
		++index[val];
	}

	for(i=1; i<max+1; ++i)
	{
		index[i] += index[i-1];		//updating the index array such that each value is a sum
									//of its former value and the value at preceeding index
	}

	for (i=0; i<n; ++i)
	{
		p[index[arr[i]]-1] = arr[i];
		--index[arr[i]];
	}

	for(i = 0; i<max; ++i)
	{
		arr[i] = p[i];
	}

	i=0;
	while(i<n){
		cout<<p[i]<<" ";
		i++;
	}

	return 0;
}
