n = int(input())

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

num = str(factorial(n))
cnt = 0
for i in range(len(num)-1, -1, -1): 
    if num[i] == '0':
        cnt += 1
    else:
        break

print(cnt)
