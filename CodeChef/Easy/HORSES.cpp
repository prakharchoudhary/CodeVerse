#include <iostream>
#include <cstdlib>

int min_diff(long int S[], int f, int l);

int main(){
	int T, size, i;
	std::cin>>T;
	while(T)
	{
		long int S[5000];
		std::cin>>size;
		for(i=0; i<size; i++)
		{
			std::cin>>S[i];
		}
		min_diff(S, 0, size);
		T--;
	}
}

int min_diff(long int S[5000], int f, int l)
{
	long int min = 1000000000, temp;
	for(int j=0; j<l-1; j++){
		for(int k = j+1; k<l; k++){
			temp = std::abs (S[j] - S[k]);
			if(temp < min)
				min = temp;
		}
	}
	std::cout<<min<<std::endl;
	return 0;
}