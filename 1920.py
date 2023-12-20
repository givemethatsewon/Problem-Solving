#from bisect import bisect_left, bisect_right

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# def find_x(arr,x):
#     #cnt = bisect_right(arr,x) - bisect_left(arr,x)
#     if cnt == 0:
#         return 0
#     else:
#         return 1
    
# n_list.sort()
# for m in m_list:
#     print(find_x(n_list,m))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n_list.sort()   
for m in m_list:
    print(binary_search(n_list, m, 0, n-1))