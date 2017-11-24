import time
import sys
from pprint import pprint
import random

def mk(i,j):
	return str(i)+','+str(j)

def lcs_length(a,b):
	m = len(a)
	n = len(b)
	lengths = [[0 for _ in range(n+1)] for _ in range(m+1)]
	for i, x in enumerate(a):
		for j, y in enumerate(b):
			if x == y:
				lengths[i+1][j+1] = lengths[i][j] + 1
			else:
				lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
	result = ""
	x, y = len(a), len(b)
	while x != 0 and y != 0:
	    if lengths[x][y] == lengths[x-1][y]:
	        x -= 1
	    elif lengths[x][y] == lengths[x][y-1]:
	        y -= 1
	    else:
	        assert a[x-1] == b[y-1]
	        result = str(a[x-1]) + result
	        x -= 1
	        y -= 1
	return result

def main():
	# X = ['A', 'B', 'D', 'B', 'C', 'A', 'B']
	# Y = ['B', 'A', 'C', 'A', 'B', 'A']
	X = [random.randint(0, 10) for _ in xrange(1000)]
	Y = [random.randint(0, 10) for _ in xrange(980)]
	start = time.time()
	print(lcs_length(X, Y))
	print("{:.4f} seconds".format(time.time()-start))

if __name__ == '__main__':
	main()
