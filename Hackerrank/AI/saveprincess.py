def displayPathtoPrincess(n,grid):
	# find location of p and m.
	for i in range(n):
		for j in range(n):
			if grid[i][j] == 'p':
				p = [i,j]
			elif grid[i][j] == 'm':
				m = [i,j]
	
	if m[0] > p[0]:
		printStep("UP",(m[0] - p[0]))
	elif m[0] < p[0]:
		printStep("DOWN",(p[0] - m[0]))		
	if m[1] > p[1]:
		printStep("LEFT", (m[1] - p[1]))
	elif m[1] < p[1]:
		printStep("RIGHT",(p[1] - m[1]))

def printStep(step, num):
	for i in range(num):
		print step
    
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)