 a = [100, 13, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

def find_max_cross_subarray(A, low, mid, high):
	left_sum = -54168742514
	max_left = low
	summ = 0
	i = mid
	while(i>=low):
		summ = summ + A[i]
		if summ>left_sum:
			left_sum = summ
			max_left = i
		i = i - 1

	right_sum = -54168742514
	summ = 0
	max_right = high
	j = mid+1
	while(j<=high):
		summ = summ + A[j]
		if right_sum >summ:
			right_sum = summ
			max_right = j
		j = j + 1
	return(max_left, max_right, left_sum+right_sum)

def find_maximum_subarray(A,low,high):
	if high==low:
		return(low, high, A[low])
	else:
		mid = (low + high)/2
		(left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
		(right_low, right_high, right_sum) = find_maximum_subarray(A, mid+1, high)
		(cross_low, cross_high, cross_sum) = find_max_cross_subarray(A, low, mid, high)

	if left_sum>=right_sum and left_sum>=cross_sum:
		return (left_low, left_high, left_sum)
	elif right_sum>=left_sum and right_sum>=cross_sum:
		return (right_low, right_high, right_sum)
	else:
		return (cross_low, cross_high, cross_sum)

print find_maximum_subarray(a, 0, 16)