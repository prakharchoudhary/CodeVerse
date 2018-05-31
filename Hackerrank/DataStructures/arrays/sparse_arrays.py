x = int(raw_input())
s = []
for i in range(x):
	s.append(raw_input())

def check(c):
	count = 0
	for i in s:
		if i==c:
			count+=1
	return count

q = int(raw_input())
for j in range(q):
	c = raw_input()
	print check(c)
