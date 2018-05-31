
T = int(raw_input())

while T:
	N, k = map(int, raw_input().split(' '))
	buckets = map(int, raw_input().split(' '))
	operations = 0
	for i in buckets:
		rem = i%k
		if i<=k:
			rem = k-i
		elif rem>(k/2):
			rem = k - rem
		operations += rem
	print operations
	T -= 1
	