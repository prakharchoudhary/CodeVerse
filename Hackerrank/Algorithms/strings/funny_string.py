for i in range(int(raw_input())):
    x = raw_input()
    y = x[::-1]
    c = 0
    for i in range(1,len(x)):
        if abs(ord(x[i]) - ord(x[i-1])) == abs(ord(y[i]) - ord(y[i-1])):
            c += 1
    if c == len(x) - 1:
        print "Funny"
    else:
        print "Not Funny"