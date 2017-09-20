import os
import sys
import random

# To heapify the subtree rooted at i
def max_heapify(arr, n, i):
	'''
	arr: the unsorted array
	n: size of heap
	i: index
	'''
	largest = i
	left = 2*i + 1
	right = 2*i + 2

	# check if the left child exists and is it greater than the root
	if left < n and arr[left] > arr[largest]:
		largest = left

	# check if the right child exists and is it greater than the root
	if right < n and arr[right] > arr[largest]:
		largest = right

	# Change the root; if needed
	if largest!=i:
		arr[i], arr[largest] = arr[largest], arr[i]
		max_heapify(arr, n, largest)

def heapSort(arr):
	n = len(arr)

	# Build a max heap
	for i in range(n, -1, -1):
		max_heapify(arr, n, i)

	# Now extract the elements; one by one
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		max_heapify(arr, i, 0)


options = '''
Enter the following choices:

python heapsort.py <option>

-i : to insert a new array.

-r : to generate a random array and output the sorted array.
'''

def main():

	if len(sys.argv)>1:
		if sys.argv[1] == '-i':
			print("Enter the unsorted array:\n")
			arr = map(int, raw_input().strip().split(' '))

		elif sys.argv[1] == '-r':
			arr = [random.randint(1,20) for i in range(1, 21)]
			print arr
		else:
			print(options)
			return
	else:
		print(options)
		return

	heapSort(arr)
	print("Sorted array is: ")
	print arr

if __name__ == "__main__":
	main()