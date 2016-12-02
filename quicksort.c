#include <stdio.h>

/*function to swap to elements*/
void swap(int *a, int *b){
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

/*function takes the last element as
pivot, places it at its correct place in
sorted array, places all the small elements
to its left and larger elemnts to its right*/ 
int partition(int arr[], int low, int high)
{
	int j;
	int pivot = arr[high];
	int i = low-1;
	for(j=low; j<=high-1; j++){

		/*if current element is smaller than
		or equal to the pivot*/
		if(arr[j]<=pivot){
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i+1], &arr[high]);
	return (i+1);
}

void quicksort(int arr[], int low, int high){
	int pi;
	if(low<high){
		/*pi is the partitioning index,
		arr[p] is now at right place*/
		pi = partition(arr, low, high);
		quicksort(arr, low, pi-1);
		quicksort(arr, pi+1, high);
	}
}

void printArray(int arr[], int size){
	int i;
	for(i=0; i<size; i++)
		printf("%d ", arr[i]);
	printf("\n");
}

int main()
{
	int size, arr[20], i;
	printf("Enter the size to array to be sorted: ");
	scanf("%d", &size);
	printf("Enter the array to be sorted: ");
	for(i = 0; i<size; i++)
		scanf("%d", &arr[i]);
	quicksort(arr, 0, size-1);
	printf("The sorted array:\n");
	printArray(arr, size);
	return 0;
}