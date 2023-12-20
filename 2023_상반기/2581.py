m = int(input())
n = int(input())
sosu = []
if m == 1:
    m = 2
    
for num in range(m,n+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        sosu.append(num)

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(sosu[0])