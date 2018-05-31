import random
import sys
import time
from pprint import pprint

def make_key(i,j):
    return str(i)+','+str(j)

def matrix_chain_order(p):
    n = len(p)-1
    m, s = {}, {}
    for i in xrange(1, n+1):
        m[make_key(i, i)] = 0
    for l in xrange(2, n+1):
        for i in xrange(1, n-l+2):
            j = i+l-1
            m[make_key(i, j)] = sys.maxint
            for k in xrange(i, j):
                q = m[make_key(i, k)]+m[make_key(k+1, j)]+p[i-1]*p[k]*p[j]
                if q<m[make_key(i, j)]:
                    m[make_key(i, j)] = q
                    s[make_key(i, j)] = k
    return m, s

def get_optimal_parens(s, i, j):
    res = ''
    if i == j:
        return "A"+str(j)
    else:
        res += "("
        res += get_optimal_parens(s, i, s[make_key(i, j)])
        res += get_optimal_parens(s, s[make_key(i, j)]+1, j)
        res +=  ")"
        return res

def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == '-c':
			p = map(int, raw_input("Enter the chain: ").split(' '))
	else:
		p = [40, 20, 30, 10, 30]
	m, s = matrix_chain_order(p)
	print 'Optimal Paranthesization is:', m[make_key(1, len(p)-1)]
	print 'Optimal Cost is: ', get_optimal_parens(s, 1, len(p)-1)

if __name__ == '__main__':
	main()



