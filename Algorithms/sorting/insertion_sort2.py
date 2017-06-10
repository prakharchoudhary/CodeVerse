#using insertion sort, sort the given array [31, 41, 29, 56, 41, 58] but in non increasing order
array = [31, 41, 29, 56, 41, 58]

print array
def insertionSort(arr):
	for j in range(1,len(arr)):
		key = arr[j]
		i = j-1
		while i>=0 and arr[i]<key:
			#just change the sign in the arr[i]>key to arr[i]<key.
			arr[i+1] = arr[i]
			i = i-1  
		arr[i+1] = key
	return arr		
print insertionSort(array)