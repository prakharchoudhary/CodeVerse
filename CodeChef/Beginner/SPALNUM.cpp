#include<iostream>
#include<cstring>
using namespace std;

int check_pal(int x)
{
	int arr[9];
	int temp = x;
	int i = 0;
	int len; 
	while(temp)
	{
		arr[i] = temp%10;
		temp = temp/10;
		i++;
	}

	len = i;
	
	for(i=0; i<len; i++)
	{
		if(arr[i] != arr[len-i-1])
			return 0;
	}

	return 1;

}

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int l, r, sum=0, i;
		cin>>l>>r;
		for(i = l; i<=r; i++)
		{
			if(check_pal(i))
			{
				sum += i;
			}
		}
		cout<<sum<<"\n";
	}
	return 0;
}