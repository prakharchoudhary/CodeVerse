#include<iostream>
using namespace std;

int main()
{
	int n, i, num[100000];
	bool cond;
	while(1)
	{
		cin>>n;
		if(n!=0)
		{	for(i=1; i<=n; i++){
				cin>>num[i];
			}

			cond = true;
			for(i = 1; i<=n; i++){
				if(i == num[num[i]])
					cond = true;
				else
				{
					cond = false;
					break;
				}
			}

			if(cond == true)
				cout<<"ambiguous\n";
			else
				cout<<"not ambiguous\n";				 
		}
		else
		{
			break;
		}

	}
	return 0;
} 	