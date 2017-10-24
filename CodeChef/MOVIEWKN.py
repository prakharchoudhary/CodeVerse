T = int(raw_input())

while T:
	size = int(raw_input())
	L = map(int, raw_input().split(' '))
	R = map(int, raw_input().split(' '))
	prod = [L[i]*R[i] for i in range(len(L))]
	max_prod = max(prod)
	arg_max = []
	for i in range(len(prod)):
		if prod[i]==max_prod:
			arg_max.append(i)
	elem_R = [R[i] for i in arg_max]
	max_R = max(elem_R)
	final_l = [R.index(i) for i in elem_R if i==max_R]
	print final_l[0]+1
	T -= 1