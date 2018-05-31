#include<iostream>
#include<vector>

using namespace std;

int fit(long int arr[], int s)
{
	long int i;
	for(i=0; i<s; i++)
	{
		if(arr[i] < 0)
			return 0;
	}
	return 1;
}

int main(){
	int T;
	cin>>T;
	while(T--)
	{
		int s, i, f, b;
		cin>>s;
		long int fingers[s], sheath[s];
		long int front[s], back[s];
		for(i=0; i<s; i++)
		{
			cin>>fingers[i];
		}
		for(i=0; i<s; i++)
		{
			cin>>sheath[i];
		}
		for(i=0; i<s; i++)
		{
			front[i] = sheath[i] - fingers[i];
			back[i] = sheath[s-i-1] - fingers[i];
		}
		f = fit(front, s);
		b = fit(back, s);
		if(f || b){
			if(f && b){
				cout<<"both"<<endl;
			}
			else if(f)
				cout<<"front"<<endl;
			else
				cout<<"back"<<endl;
		}
		else{
			cout<<"none"<<endl;
		}
	}
}