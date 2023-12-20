import sys
input = sys.stdin.readline

n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]
#정렬
pairs.sort(key= lambda x : (x[1],x[0]))
#출력
for pair in pairs:
    print(*pair, sep=' ')
