for t in range(int(raw_input())):
    v = raw_input()
    y = list(v)
    def alternate(z):
        d = 0
        j = 0
        for i in xrange(1, len(z)):
            if z[i] == z[j]:
                d = d+1
            else:
                j = i
        return d
    print alternate(y)