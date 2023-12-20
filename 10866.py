import sys
from collections import deque

input = sys.stdin.readline

deq = deque()
n = int(input())

def empty(x):
    if not bool(x):
        return 1
    return 0

for _ in range(n):
    order = input().rstrip()
    if 'push_front' in order:
        data = order.split()[-1]
        deq.appendleft(data)
    
    elif 'push_back' in order:
        data = order.split()[-1]
        deq.append(data)
    
    elif order == 'empty':
        print(empty(deq))
    
    elif order == 'pop_front':
        if empty(deq):
            print(-1)
        else:
            print(deq.popleft())
    
    elif order == 'pop_back':
        if empty(deq):
            print(-1)
        else:
            print(deq.pop())
    
    elif order == 'front':
        if empty(deq):
            print(-1)
        else:
            print(deq[0])

    
    elif order == 'back':
        if empty(deq):
            print(-1)
        else:
            print(deq[-1])
    
    elif order == 'size':
        print(len(deq))