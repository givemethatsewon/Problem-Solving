import sys
input = sys.stdin.readline

n,m = map(int, input().split())
original = []
count = []

for _ in range(n):
    original.append(input().rstrip())

for a in range(n-7):
    for b in range(m-7):    #a,b == 시작점
        draw1 = 0 #첫 번째 타일 흰색일 경우
        draw2 = 0 #첫 번째 타일 검은색일 경우
        
        for i in range(a,a+8):
            for j in range(b,b+8):  #시작점을 기준으로 8X8 체스판 탐색
                if (i+j) % 2 == 0:  #홀수번째 지점
                    if original[i][j] == 'W': 
                        draw1 += 1
                    if original[i][j] == 'B':
                        draw2 += 1
                else:   #짝수번째 지점
                    if original[i][j] == 'B': #W로 시작했으면 그 다음 타일 B여야 함
                        draw1 += 1
                    if original[i][j] == 'W': #B로 시작했으면 그 다음 타일 W여야 함
                        draw2 += 1
#더 적게 draw증가한 것은 체스판의 규칙을 어긴 개수를 의미
        count.append(min(draw1,draw2))  #더 적게 draw증가 -> 최소 수정 횟수 이므로 min 사용
print(min(count)) #여러가지 8X8 중 최소이므로 min 사용
