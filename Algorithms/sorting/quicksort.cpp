#include <iostream>
using namespace std;

void swap(int *a, int *b)
{
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

int partition(int *arr, int low, int high)
{
	int i, j, pivot;
	pivot = arr[high];
	i = low-1;

	for(j=low; j<high; j++){

		/* 
		if current element is smaller than or
		equal to pivot
		*/
		if(arr[j]<=pivot){
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i+1], &arr[high]);
	return (i+1);
}

int quickSort(int *arr, int low, int high)
{
	int pi;
	if(low<high)
	{
		pi = partition(arr, low, high);
		quickSort(arr, low, pi-1);
		quickSort(arr, pi+1, high);
	}
}

void printArray(int arr[], int size){
	int i;
	for(i=0; i<size; i++)
		cout<<arr[i]<<" ";
	cout<<"\n";
}

int main()
{
	int size, arr[20], i;
	cout<<"Enter the size to array to be sorted: ";
	cin>>size;
	cout << "Enter the array to be sorted: ";
	for(i = 0; i<size; i++)
		cin>>arr[i];
	quickSort(arr, 0, size-1);
	cout<< "The sorted array:\n";
	printArray(arr, size);
	return 0;
}