// Ciel and A-B Problem | Problem Code: CIELAB
#include <iostream>

int main()
{
	int a, b;
	std::cin>>a>>b;
	int c;
	c = a-b;
	if(c%10 <= 8)
		c += 1;
	else
		c -= 1;
	std::cout<<c;
}