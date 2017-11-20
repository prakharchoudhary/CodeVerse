import random
import sys
import time

def bottom_up_cut_rod(p, n):
	r = range(n+1)
	r[0] = 0
	for j in range(1,n+1):
		q = sys.maxint * -1
		for i in range(0, j):
			q = max(q, p[i]+r[j-i-1])
		r[j] = q
	return r[n]

def main():
	if len(sys.argv)==1:	
		arr = map(int, raw_input('Enter the costs: ').strip().split(' '))
		r = len(arr)
		start = time.time()
		maxCost = bottom_up_cut_rod(arr, r)
		end = time.time()
		print("Rod length: %d"%r)
		print("The maximum cost that can be obtained is: %d"%maxCost)
		print("Time Taken: %fms\n"%(end-start))

	else:
		l = [5, 10, 15, 20, 25]
		for r in l:
			arr = [random.randint(1, r) for i in range(r)]
			print arr
			start = time.time()
			maxCost = bottom_up_cut_rod(arr, r)
			end = time.time()
			print("Rod length: %d"%r)
			print("The maximum cost that can be obtained is: %d"%maxCost)
			print("Time Taken: %fms\n"%(end-start))
			time.sleep(1)

if __name__=='__main__':
	random.seed(67)
	main()