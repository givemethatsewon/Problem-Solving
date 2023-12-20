from math import sqrt
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0 or n == 1 or n == 2:
        n = 2
    elif n % 2 == 0:
        n += 1
    check = 3
    sq = sqrt(n)
    while check <= sq:
        if n % check == 0:
            n += 2
            check = 3
            sq = sqrt(n)
        else:
            check += 2
    print(n)
