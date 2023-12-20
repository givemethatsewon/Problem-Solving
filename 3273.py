import sys
input = sys.stdin.readline

counts = [0 for i in range(1000001)]
#인덱스 = 실제 수
#값 = 인덱스에 해당하는 숫자의 개수

n = int(input())    #수열의 크기
nums = list(map(int, input().split()))
#수의 개수 counts에 입력
for num in nums:
    counts[num] += 1

x = int(input()) #a + b = x를 만족하는 순서쌍의 개수

result = 0
for num in nums:
    if x - num <= 1000000:
        result += (counts[num] * counts[x - num])

print(result//2) 
    
