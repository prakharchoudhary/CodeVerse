#include <iostream>

int main()
{
	int T, i, n, m, fnum;
	// int fjobs[1000];
	std::cin>>T;
	while(T)
	{
		int jobs[1000] = {0};
		int chef = 1, c = 0, a = 0, c_j[1000], a_j[1000]; 
		std::cin>>n>>m;
		for(i = 0; i<m; i++)
		{
			std::cin>>fnum;
			jobs[fnum - 1] = 1; 
		}
		for(i=0; i<n; i++){
			// std::cout<<jobs[i]<<" ";
			if(jobs[i] == 0)
			{
				if(chef){
					c_j[c++] = i+1;
					chef = 0;
				}
				else{
					a_j[a++] = i+1;
					chef = 1;
				}
			}
		}

		for(int p = 0; p<c; p++)
		{
			std::cout<<c_j[p]<<" ";
		}
		std::cout<<std::endl;
		for(int p = 0; p<a; p++)
		{
			std::cout<<a_j[p]<<" ";
		}
		std::cout<<std::endl;
		T --;
	}
}