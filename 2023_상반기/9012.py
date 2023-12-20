import sys
input = sys.stdin.readline

t_case = int(input())

for case in range(t_case):
    ps = input().rstrip()    
    stack = []
    
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
