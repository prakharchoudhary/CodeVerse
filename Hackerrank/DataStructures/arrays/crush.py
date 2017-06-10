n, m = map(int, raw_input().strip().split(' '))

listt = [0 for i in range(n+1)]
maxx = 0
x=0

for _ in range(m):
	p,q,inc = map(int, raw_input().split(' '))
	listt[p] += inc
	if q+1<=n: listt[q+1] -= inc

for i in range(1,n+1):
	x += listt[i]
	if maxx<x: maxx = x
print maxx