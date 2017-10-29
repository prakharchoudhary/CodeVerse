#include<iostream>
#include<cmath>
using namespace std;

int find_menu(int n, int count)
{
	int i, flag = 0;
	for(i=0; i<12; i++){
		
		if((n-pow(2,i))<0)
			break;

		else if((n - pow(2,i)) == 0){
			flag = 1;
			break;
		}
	}
	if(flag)
		n = n - pow(2,i);
	else
		n = n-pow(2,i-1);
	
	count++;
	
	if(n == 0)
		return count;
	else{
		find_menu(n,count);
	}
}

int main()
{
	int T;
	cin>>T;
	while(T){
		int n,count=0, ans;
		cin>>n;
		ans = find_menu(n, count);
		cout<<ans<<"\n";
		T--;
	}
}