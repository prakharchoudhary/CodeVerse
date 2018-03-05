#include <iostream>
#include<vector>
#include<climits>

int main()
{
	int T;
	std::cin>>T;
	while(T--){
		int n, i, max=INT_MAX, count=0;
		std::cin>>n;
		std::vector<int> cars(n);
		for(i=0; i<n; i++){
			std::cin>>cars[i];
		}
		for(i=0; i<n; i++){
			if(cars[i] <= max){
				count++;
				max = cars[i];
			}
		}
		std::cout<<count<<std::endl;
	}
}