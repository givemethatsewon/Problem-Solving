n = int(input())
a = b = 0   #a는 5kg 개수, b는 3kg 개수
possible = []
while 5*a <= n:
    while 5*a + 3*b <= n:
        if 5*a + 3*b == n:
            possible.append(a + b)
        b += 1
    a += 1
    b = 0

if possible:
    print(min(possible))
else:
    print(-1)