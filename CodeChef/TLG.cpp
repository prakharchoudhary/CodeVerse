#include <iostream>
using namespace std;
#define SIZE 10000

int main()
{
	int n,a=0, b=0,l=0,w,fl=0,fw, diff;
	cin>>n;
	while(n)
	{
		int c,d;
		cin>>c>>d;
		a += c;
		b +=d;
		diff = a - b;
		if(diff>0)
		{
			l = diff;
			w = 1;
		}
		else{
			l = -1*diff;
			w = 2;
		}

		if(l>fl){
			fl = l;
			fw = w;
		}
		n--;		
	}
	cout<<fw<<" "<<fl;
	return 0;
}