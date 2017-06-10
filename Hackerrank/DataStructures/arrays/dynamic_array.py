n, q = raw_input().split(' ')
lastans = 0
n = int(n)
q = int(q)

seq = [x for x in range(n)]
for i in range(n):
	seq[i] = []

for i in range(q):
	query = map(int, raw_input().split(' '))
	
	if query[0] == 1:
		# print query[2]
		s = (query[1] ^ lastans)%n
		seq[s].append(query[2])

	elif query[0] == 2:
		s = (query[1] ^ lastans)%n
		lastans = seq[s][query[2]%len(seq[s])]
		print lastans