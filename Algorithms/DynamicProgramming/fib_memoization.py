def fib(n, lookup):
	if n==0 and n==1:
		lookup[n] = n
	if lookup[n] is None:
		lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
	return lookup[n]

def main():
	n=34
	# Handles till n = 100
	lookup = [None]*(101)	
	print "Fibonacci Number is ", fib(n, lookup)

if __name__=='__main__':
	main()
