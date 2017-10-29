#include<iostream>
using namespace std;

int main()
{
	int T, n, i, j, arr[100][100], max, flag;
	cin>>T;
	while(T)
	{
		cin>>n;
		flag=1;
		for(i =0; i<n; i++){
			for(j = 0; j <= i; j++){
				cin>>arr[i][j];
			}
		}

		for (i=1; i<n; i++){
			for(j=0; j<=i; j++){
				if(j==0)
					arr[i][j] += arr[i-1][j];
				else if(j == i){
					arr[i][j] += arr[i-1][j-1];
				}
				else
				{
					arr[i][j] += (arr[i-1][j] > arr[i-1][j-1] ? arr[i-1][j]:arr[i-1][j-1]);
				}
			}
		}
		max = arr[n-1][0];
		for(i=0; i<n; i++){
			if (arr[n-1][i] > max)
				max = arr[n-1][i];
		}
		cout<<max<<"\n";
		T--;				 
	}
	return 0;
} 	