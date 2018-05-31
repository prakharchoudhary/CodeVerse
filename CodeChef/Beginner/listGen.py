import random
def randomTest(n):
	l = []
	for i in range(1, n):
		a = []
		for j in range(0,2):
			a.append(i*random.randint(1,10))
		if a[0] == a[1]:
			a[random.randint(0,1)] += random.randint(1,10)
		l.append(a)
	return l

if __name__ == '__main__':
	n = int(raw_input("Enter a range: "))
	data = randomTest(n)	
	file = open("C:/Users/Prakhar/Desktop/file.txt", "w+")
	for i in data:
		x = "%s %s\n"%(i[0], i[1])
		file.write(x) 
	print "All done!"
	file.close()
