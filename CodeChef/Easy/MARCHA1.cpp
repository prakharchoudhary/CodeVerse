#include <iostream>

using namespace std;

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
		// apply 0-1 knapsack to find the suitable subset.
	}
	return 0;
}