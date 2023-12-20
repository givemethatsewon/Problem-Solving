import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

#중복 제거하고 오름차순으로 리스트 정렬
sorted_nums = sorted(list(set(nums)))

#검색할 때 시간복잡도를 줄이기 위해 딕셔너리에 저장
dic_nums = dict()
for idx,num in enumerate(sorted_nums):
    dic_nums[num] = idx

for num in nums:
    print(dic_nums[num], end=' ')
