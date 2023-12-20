from bisect import bisect_right, bisect_left
import sys
input = sys.stdin.readline

t = int(input())

#def binary_search(array, start, end, target):
#    while start <= end:
#        mid = (start + end) // 2
#        
#        if array[mid] > target:
#            end = mid - 1
#        else:
#            ans = mid
#           start = mid + 1
#    return ans


for _ in range(t):
    a, b = map(int, input().split())    
    a_nums = list(map(int, input().split()))
    b_nums = list(map(int, input().split()))

    b_nums.sort()
    cnt = 0
    length = len(b_nums)
    for a in a_nums:
        target_cnt = bisect_right(b_nums, a-1)
        cnt += target_cnt
    
    print(cnt)