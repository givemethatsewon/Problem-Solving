import sys
input = sys.stdin.readline

n, c = map(int, (input().split()))
x_list = [int(input()) for _ in range(n)]
x_list.sort()

start = 1
end = x_list[-1] - x_list[0]
while start <= end:
    mid = (start + end) // 2
    s_point = x_list[0] #starting point
    routers = c - 1 #첫번째 공유기 s_point에 설치했으므로
    for x in x_list:
        if x - s_point >= mid:
            s_point = x
            routers -= 1
        
        if routers == 0: break  #공유기 다 썼으면 더 돌아볼 필요 없으므로 탈출
    
    if routers > 0:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
print(ans)
