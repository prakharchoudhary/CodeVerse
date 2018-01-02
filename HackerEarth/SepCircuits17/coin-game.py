T = int(raw_input())
def is_even(x):
    if x%2==0:
        return 1
    return 0

while T:
    c = 0; a = 1
    s = int(raw_input())
    piles = map(int, raw_input().strip().split(' '))
    for i in range(s):
        while is_even(piles[i]):
            piles[i]=piles[i]/2
            c,a = a,c
    if c:
        print "Charlie"
    else:
        print "Alan"
    T -= 1