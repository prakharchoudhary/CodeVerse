N,k,Q = map(str, raw_input().strip().split(' '))
Q = int(Q)
net_nums = 1
while Q:
    l, r = map(int, raw_input().strip().split(' '))
    status = False
    for i in range(l, r+1):
        i = str(i)
        if len(i) == len(N):
            count = sum(1 for a, b in zip(i, N) if a != b)
            if count <= k:
                status = True
    if status:
        net_nums += 1
    Q -= 1

print net_nums