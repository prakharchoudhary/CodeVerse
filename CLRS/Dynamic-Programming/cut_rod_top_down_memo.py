import random
import sys
import time

def memoized_cut_rod(p, n):
	r = [(sys.maxint-1)*-1 for i in xrange(n)]
	return memoized_cut_rod_aux(p,n,r)

def memoized_cut_rod_aux(p, n, r):
	if r[n-1]>=0:
		return r[n-1]
	if n==0:
		q = 0
	else:
		q = (sys.maxint-1)*-1
		for j in range(1, n):
			q = max(q, p[j]+memoized_cut_rod_aux(p, n-j-1, r))
	r[n-1] = q
	return q

def main():
	if len(sys.argv)==1:	
		arr = map(int, raw_input('Enter the costs: ').strip().split(' '))
		r = len(arr)
		start = time.time()
		maxCost = memoized_cut_rod(arr, r)
		end = time.time()
		print("Rod length: %d"%r)
		print("The maximum cost that can be obtained is: %d"%maxCost)
		print("Time Taken: %fms\n"%(end-start))

	else:
		l = [5, 10, 15, 20, 25]
		for r in l:
			arr = [random.randint(1, r) for i in range(r)]
			start = time.time()
			maxCost = memoized_cut_rod(arr, r)
			end = time.time()
			print("Rod length: %d"%r)
			print("The maximum cost that can be obtained is: %d"%maxCost)
			print("Time Taken: %fms\n"%(end-start))
			time.sleep(1)

if __name__=='__main__':
	main()