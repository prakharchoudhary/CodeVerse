#include<iostream>
using namespace std;

int main(){
	int T, N, count=0;
	cin>>T>>N;
	while(T){
		unsigned int n;
		cin>>n;
		if(n%N==0)
			count++;
		T--;
	}
	cout<<count<<"\n";
	return 0;
}