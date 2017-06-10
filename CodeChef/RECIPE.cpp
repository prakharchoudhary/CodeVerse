#include<iostream>
using namespace std;

int minima(int arr[50], int n)
{
	int i,  min = arr[0];
		for(i=0; i<n; i++){
			if(min>arr[i])
				min = arr[i];
		}
	return min;
}

int common(int arr[50], int s, int x)
{
	int i, j, check, hcf;
	for(i=1; i<=x; i++){
		check = 1;
		for(j = 0; j<s; j++){
	  		if(arr[j]%i != 0)
				check = 0;
		}
		if (check == 1)
			hcf = i;
	}
	return hcf;
}

int main()
{
	int T;
	cin>>T;
	while(T)
	{
		int n, arr[50], hcf;
		cin>>n;
		for(int i=0; i<n; i++){
			cin>>arr[i];
		}

		int min = arr[0];
		for(int i=0; i<n; i++){
			if(min>arr[i])
				min = arr[i];
		}

		// to be optimised
		hcf = common(arr, n, min);
		

		for(int i=0; i<n; i++){
			arr[i] = arr[i] / hcf;
		}

		for(int i=0; i<n; i++){
			cout<<arr[i]<<" ";
		} 
		cout<<"\n";
		--T;
	}
	return 0;
}