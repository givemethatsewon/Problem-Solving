import math

A,I = map(int,input().split())

n = 1
while math.ceil(n/A) < I:
    n += 1

print(n)
