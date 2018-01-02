/*
Problem statement:

For any given positive integer, sum up all its digits until
we obtain a single digit number; then print its square root.
*/
#include<iostream>
#include <cmath>

using namespace std;

int sumNum(long int number){
	int rem;
	int total = 0;
	while(number != 0){
		rem = number % 10;
		total += rem;
		number -= rem;
		number /= 10;
	}
	return total;
}

int digital_root(long int number){
	while(number > 9){
		number = digital_root(number);
	}
	return number;
}

int main(){
	cout<<"Digital root of 1233: "<<digital_root(1233)<<endl;
	cout<<"Digital root of 65536: "<<digital_root(65536)<<endl;
	cout<<"Digital root of 9199999: "<<digital_root(9199999)<<endl;
	cout<<"Digital root of 96999999: "<<digital_root(96999999)<<endl;
	return 0;
}

