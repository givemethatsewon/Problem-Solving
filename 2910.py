n, c = map(int, input().split())
nums = list(map(int, input().split()))

frequency = dict()
cnt = 0 
for num in nums:
    cnt += 1
    if num not in frequency:
        frequency[num] = [1, cnt]
    else:
        frequency[num] = [frequency[num][0]+1, frequency[num][1]]

#value값을 기준으로 내림차순 정렬
s_list = sorted(frequency.items(), key = lambda x : (-x[1][0], x[1][1]))

for k,v in s_list:
    for _ in range((v[0])):
        print(k, end=' ')