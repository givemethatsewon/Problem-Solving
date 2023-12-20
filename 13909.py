n = int(input())
start = 1
cnt = 0

#n보다 작은 제곱수의 개수 구하기
while start**2 <= n:
    cnt += 1
    start += 1

print(cnt)
