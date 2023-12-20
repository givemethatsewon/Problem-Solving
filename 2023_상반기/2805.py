import sys
input = sys.stdin.readline

n, target = map(int, input().split())
trees = list(map(int, input().split()))

#이분탐색으로 적절한 cutter길이 찾기
start = 0
end = max(trees)
ans = 0

while start <= end:
    cutter = (start + end) // 2
    total = 0   #잘린 나무들의 합 저장
    
    for tree in trees:
        if tree > cutter:
            total += (tree - cutter)
    
    if total < target:
        end = cutter - 1
    else:
        ans = cutter
        start = cutter + 1

#답 출력
print(ans)