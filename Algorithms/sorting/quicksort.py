def partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]

	for j in range(low, high):

		# If current element smaller than or
		# equal to pivot
		if arr[j] <= pivot:
			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high]  = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if low<high:

		pi = partition(arr, low, high)

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr = map(int, raw_input("Enter the array to be sorted:\n").strip().split(' '))
n = len(arr)
quickSort(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d " %arr[i]),