n = int(input())    #들어올 숫자의 개수
nums = list(map(int, input().split()))
sosu_cnt = 0
for num in nums:
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        sosu_cnt += 1

if 1 in nums:
    sosu_cnt -= 1

print(sosu_cnt)