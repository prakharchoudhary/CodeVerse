l = int(raw_input())
boosters = map(int, raw_input().strip().split(' '))
trueval = []
for i in range(l):
    if boosters[i]+i+1 > l:
        trueval.append(i)

print min(trueval)+1