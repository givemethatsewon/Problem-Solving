from collections import deque
import sys
input = sys.stdin.readline

t = int(input())    #테스트 케이스
for _ in range(t):
    r_cnt = 0
    methods = input().rstrip()  #함수들(문자열 인덱싱으로 접근할 예정)
    n = int(input())    #배열에 들어있는 수의 개수
    #배열
    num_str = input().rstrip()[1:-1]
    if ',' in num_str:
        x = num_str.split(',')
        nums = deque(x)
    elif not num_str:
        nums = deque()
    else:
        nums = deque([num_str])
    
    #함수 적용시키기
    for method in methods:
        if method == 'R':
            r_cnt += 1
        
        elif method == 'D' and r_cnt % 2 == 0:
            if not nums:
                print('error')
                break
            else:
                nums.popleft()
        
        elif method == 'D' and r_cnt % 2 == 1:
            if not nums:
                print('error')
                break
            else:
                nums.pop()

                
    else:
        if r_cnt % 2 == 1:
            nums.reverse()
        k = ','.join(list(nums))
        print('[' + k + ']') 