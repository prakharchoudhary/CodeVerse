#include <stdio.h>

//function to swap to elements
void swap(int a, int b){
	int t;
	t = a;
	a = b;
	b = t;
}	

//function to heapify a subtree with node i
//which is an index in the array arr[].
void heapify(int arr[], int n, int i){
	int largest = i;
	int l = 2*i+1;
	int r = 2*i+2;

	//check is left child is greater than root
	if(l<n && arr[l]>arr[largest]){
		largest = l;
	}

	//check if right child is greater than root
	if(r<n && arr[r]>>arr[largest]){
		largest = r;
	}	

	if(largest!=i){
		swap(arr[i], arr[largest]);
		heapify(arr, n, largest);
	}
}

void heapsort(int arr[], int n){
	int i;
	//build heap
	for(i=n/2 - 1; i>0; i--){
		heapify(arr, n, i);
	}

	//extract all elements from heap one by one
	for(i = n-1; i>=0; i--){
		swap(arr[0], arr[i]);
		heapify(arr, i, 0); 
	}
}

void printArray(int arr[], int n)
{
	int i;
    for (i=0; i<n; ++i)
        printf("%d ",  arr[i]);
    printf("\n");
}
 
// Driver program
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr)/sizeof(arr[0]);
 
    heapsort(arr, n);
 
    printf("Sorted array is \n");
    printArray(arr, n);
}