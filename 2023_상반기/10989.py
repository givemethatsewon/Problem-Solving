import sys
input = sys.stdin.readline

n = int(input())
count = [0 for _ in range(10001)]

for i in range(n):
    idx = int(input())
    count[idx] += 1

for idx in range(10001):
    if count[idx] != 0:
        for _ in range(count[idx]):
            print(idx)
