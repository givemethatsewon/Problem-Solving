import sys
input = sys.stdin.readline

k, n = map(int, input().split())    #이미 가지고 있는 k개의 랜선, 필요한 n개의 랜선
k_list = [int(input()) for _ in range(k)]   #가지고 있는 랜선 리스트

#이진 탐색을 위한 시작점과 끝점 설정
start = 1
end = max(k_list)

while start <= end:
    mid = (start + end) // 2
    
    total = 0   #잘린 랜선의 개수 합
    for k in k_list:
        total += (k // mid)
    
    if total < n: #잘린 랜선의 개수 합이 n개보다 작으면
        end = mid - 1
    else:   #잘린 랜선의 개수 합이 n개보다 크거나 같으면
        ans = mid
        start = mid + 1 

print(ans)