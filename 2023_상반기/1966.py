import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    n, m = map(int, input().split())
    importance = deque(list(map(int, input().split())))
    papers = deque([False for _ in range(n)])
    papers[m] = True

    cnt = 0
    while True in papers:
        prior = max(importance)
        if importance[0] != prior:
            importance.rotate(-1)
            papers.rotate(-1)
        else:
            importance.popleft()
            papers.popleft()
            cnt += 1

    ans.append(cnt)
print(*ans, sep='\n')