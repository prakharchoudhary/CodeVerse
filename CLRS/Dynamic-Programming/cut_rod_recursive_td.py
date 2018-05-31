import random
import sys
import time
 
# A recursive top-down implemetation
def cut_rod(p, n):
	if n==0:
		return 0
	q = (sys.maxint-1) * -1
	for i in range(0, n):
		q = max(q, p[i] + cut_rod(p, n-i-1))
	return q

if __name__=='__main__':
	# arr = map(int, raw_input('Enter the costs: ').strip().split(' '))
	# l = len(arr)
	l = [5, 10, 15, 20, 25]
	for r in l:
		arr = [random.randint(1, r) for i in range(r)]
		start = time.time()
		maxCost = cut_rod(arr, r)
		end = time.time()
		print("Rod length: %d"%r)
		print("The maximum cost that can be obtained is: %d"%maxCost)
		print("Time Taken: %fms\n"%(end-start))
		time.sleep(1)