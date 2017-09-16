def countSort(arr):

	# this array will store the output sorted array
	output = [0 for i in range(len(arr))]

	# this array will store the count of each element in the passed array
	count = [0 for i in range(256)]

	# store count of each character
	for i in range(len(arr)):
		count[i] += 1

	# change count[i] so that it contains the actual position for this
	# character in output array
	# for i in range(len(arr)):
	# 	count[i] += count[i-1]

	# form the output array
	for i in range(len((arr))):
		output[count[arr[i]]-1] = arr[i]
		count[arr[i]] -= 1

	return output

arr = map(int, raw_input("Enter unsorted array (max_element=255):\n").strip().split(' '))
output_arr = countSort(arr)

print "The sorted array is:\n"
print output_arr