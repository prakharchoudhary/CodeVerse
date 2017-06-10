T = int(raw_input())
while(T):
	x = raw_input()
	x = x.split('-')
	cond = True
	for i in x[2]:
		if i in x[0] or i in x[1]:
			cond = True
		else:
			cond = False
			break
	if cond == False:
		print "Unlucky Watson"
	else:
		print "Lucky Watson"
	T -= 1

