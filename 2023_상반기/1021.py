from collections import deque

n, m = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
num_list = list(map(int, input().split()))
num_deq = deque(num_list)
cnt = 0

while len(num_deq) > 0:
    if arr[0] == num_deq[0]:
        arr.popleft()
        num_deq.popleft()
    else:
        if arr.index(num_deq[0]) > len(arr) // 2:
            arr.rotate(1)
            cnt += 1
        else:
            arr.rotate(-1)
            cnt += 1
            
print(cnt)
