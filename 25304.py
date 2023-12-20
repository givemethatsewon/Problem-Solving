total = int(input())
n = int(input())
stuff_sum = 0

for stuff in range(n):
    a, b = map(int, input().split())
    stuff_sum += a * b

if total == stuff_sum:
    print('Yes')
else:
    print('No')