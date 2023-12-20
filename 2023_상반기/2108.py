import sys
input = sys.stdin.readline

n = int(input())
num_list = []
most_idxs = []
#[0,4000]에 -4000 ~ 0대응
#[4001,8000]에 1 ~ 4000대응
count = [0]*8001
for _ in range(n):
    num = int(input())
    count[num + 4000] += 1

for i in range(8001):
    #정렬된 리스트 만들기
    if count[i]:
        for _ in range(count[i]):
            num_list.append(i - 4000)    
    #최빈값 구하기 위해 숫자 저장
    most = max(count)
    if count[i] == most:
        most_idxs.append(i - 4000)

#산술평균
mean = round(sum(num_list)/n)
print(mean)
#중앙값
center = num_list[n//2]
print(center)
#최빈값
if len(most_idxs) == 1:
    print(most_idxs[0])
else:
    print(most_idxs[1])
#범위
extent = num_list[-1] - num_list[0]
print(extent)


