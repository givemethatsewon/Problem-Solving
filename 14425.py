import sys
input = sys.stdin.readline

n,m = map(int, input().split())
cnt = 0
s = set()
for _ in range(n):
    s.add(input().rstrip())

for _ in range(m):
    if input().rstrip() in s:
        cnt += 1
print(cnt)
