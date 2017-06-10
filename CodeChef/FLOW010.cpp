#include<iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	char n;
	while(T--)
	{
		cin>>n;
		if(n == 'B' || n == 'b')
			cout<<"BattleShip\n";
		else if(n == 'D' || n == 'd')
			cout<<"Destroyer\n";
		else if(n == 'C' || n == 'c')
			cout<<"Cruiser\n";
		else if(n == 'F' || n == 'f')
			cout<<"Frigate\n";
	}
	return 0;
}