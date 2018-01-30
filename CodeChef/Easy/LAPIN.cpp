#include <iostream>
#include<cstring>

using namespace std;

int main()
{
	int T, size, pos;
	string s, left, right;
	cin>>T;
	while(T--)
	{
		int flag = 1;
		cin>>s;
		size = s.length();
		if(size % 2==0){
			left = s.substr(0,size/2);
			right = s.substr(size/2, size/2);
		}
		else{
			left = s.substr(0, size/2);
			right = s.substr(size/2 + 1, size/2);
		}
		for(int i=0; i<size/2; i++)
		{
			if(right.find(left[i]) == -1){
				cout<<"NO"<<endl;
				flag = 0;
				break;
			}
			pos = right.find(left[i]);
			right.erase(pos, 1);
		}
		if(flag) cout<<"Yes"<<endl;
	}
	return 0;
}