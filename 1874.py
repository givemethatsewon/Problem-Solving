import sys

n = int(sys.stdin.readline())
stack = []
result = []
count = 1

for _ in range(n):
    data = int(sys.stdin.readline())    #다음줄 입력
    while count <= data:    #증가하는 숫자가 입력된 숫자보다 같거나 작으면
        stack.append(count) #스택에 추가
        count += 1  #숫자 1증가 시킴
        result.append('+')  #과정 기록
        #숫자가 증가하면서 입력된 숫자보다 커짐  -> while문 탈출
    if stack[-1] == data:   #스택의 last in이 입력된 숫자와 같으면
        stack.pop() #스택에서 first out
        result.append('-')  #과정 기록
    else:   #last in이 입력된 숫자와 같지 않으면
        print('NO')
        exit(0)#코드 강제종료

print(*result, sep='\n')