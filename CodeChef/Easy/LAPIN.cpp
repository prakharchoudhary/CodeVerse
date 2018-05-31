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
		int i, flag=1, left_alpha[26] = {0}, right_alpha[26] = {0};
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
		for(i=0; i<left.length(); i++){
			left_alpha[int(left[i]) - 97]++;
		}
		for(i=0; i<right.length(); i++){
			right_alpha[int(right[i]) - 97]++;
		}
		for(i=0; i<26; i++){
			if(left_alpha[i] != right_alpha[i]){
				flag = 0;
				break;
			}
		}
		if(flag)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}