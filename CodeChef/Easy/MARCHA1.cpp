#include <iostream>

using namespace std;

bool isSubsetSum(int set[], int n, int sum);

int main()
{
	int T, n, m, am, total;
	cin>>T;
	while(T--)
	{
		cin>>n>>m;
		total = 0;
		bool flag = false;
		int notes[n];
		for(int i=0; i<n; i++){
			cin>>notes[i];
		}
		if(isSubsetSum(notes, n, m))
			cout<<"Yes"<<endl;
		else
			cout<<"No"<<endl;
	}
	return 0;
}

bool isSubsetSum(int set[], int n, int sum)
{
   if (sum == 0)
     return true;
   if (n == 0 && sum != 0)
     return false;
 
   if (set[n-1] > sum)
     return isSubsetSum(set, n-1, sum);
 
   return isSubsetSum(set, n-1, sum) || 
                        isSubsetSum(set, n-1, sum-set[n-1]);
}
