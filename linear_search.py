array = [31, 41, 29, 56, 41, 58]

print array

x = int(raw_input("Which integer do u wanna search? "))

def linear_search(arr, a):
	for i in range(0,len(arr)):
		if a==arr[i]:
			result = i+1 #given us which element is it in the array.
			break
		else:
			result = "Not found."
	return result		
print linear_search(array, x)