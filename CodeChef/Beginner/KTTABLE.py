T = int(raw_input())

while T:
	size = int(raw_input())
	A = map(int, raw_input().split(' '))
	B = map(int, raw_input().split(' '))
	count = 0
	A.insert(0, 0)
	_A = [(A[i] - A[i-1]) for i in range(1, size+1)]
	for i in range(size):
		if _A[i] >= B[i]:
			count += 1
	print count
	T -= 1