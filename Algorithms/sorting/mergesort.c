#include <stdio.h>

void merge(int *arr, int l, int m, int r)
{
	int i, j, k;
	int n1 = m-l+1;
	int n2 = r-m;

	// create temp arrays
	int L[n1], R[n2];

	// Copy data to temp arrays L and R
	for(i=0; i<n1; i++)
		L[i] = arr[l+i];
	for(j=0; j<n2; j++)
		R[j] = arr[m+1+j];

	// Merge the temp arrays back into arr[l....r]
	i=0;
	j=0;
	k=l;
	while(i<n1 && j<n2)
	{
		if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
	}

	// Copy the remaining elements of L[] if there are any
	while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

	// Copy the remaining elements of R[] if there are any 
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int *arr, int l, int r)
{
	if(l<r)
	{
		// Same as (l+r)/2, but avoids overflow for
		// large l and h
		int m = l+(r-l)/2;

		// Sort first and second halves
		mergeSort(arr, l, m);
		mergeSort(arr, m+1, r);

		merge(arr, l, m, r);
	}
}

void printArray(int *arr, int size)
{
	int i;
	for(i=0; i<size; i++)
	{
		printf("%d ", arr[i]);
	}
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
	mergeSort(arr, 0, size-1);
	printf("The sorted array:\n");
	printArray(arr, size);
	return 0;
}