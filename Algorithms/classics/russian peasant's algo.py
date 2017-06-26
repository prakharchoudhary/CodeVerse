def russian(a,b):
    x = a; y = b
    z = 0
    count = 0
    while x > 0:
        if x % 2 == 1: 
        	z = z + y
        	count +=1
        y = y << 1
        x = x >> 1
    return z, count

print russian(20, 7)