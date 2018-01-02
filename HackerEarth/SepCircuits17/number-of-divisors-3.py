from math import ceil, sqrt

def factor(n):
    if n <= 1: return []
    prime = next((x for x in range(2, int(ceil(sqrt(n))+1)) if n%x == 0), n)
    return [prime] + factor(n//prime)

n = int(raw_input())
primes = factor(n)

