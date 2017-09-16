def binarySearch(arr, l, r, x):

	#Check base case
	if r>=l:

		mid = l + (r-l)/2

		# If element is present at middle
		if arr[mid] == x:
			return mid

		# if element is smaller than mid, then it must be present in the left subarray
		elif arr[mid]>x:
			binarySearch(arr, l, mid-1, x)

		# if element is greater than mid, then it must be present in the right subarray
		else:
			return binarySearch(arr, mid+1, r, x)

	else:
		return -1

# Test array
arr = [29, 31, 41, 41, 56, 58]
x = 41

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print "Element is on position %d in the array" % (result+1)
else:
    print "Element is not present in array"