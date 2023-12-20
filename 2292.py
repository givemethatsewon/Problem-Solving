user_n = int(input())

cnt = 1
stack_n = 1
n = 0
while stack_n < user_n:
    n += 1
    stack_n += n*6
    cnt += 1
print(cnt)