from math import sqrt
m = int(input())
n = int(input())
sm = sqrt(m)
sn = sqrt(n)
slist = []

for num in range(1,101):
    if num >= sm and num <= sn:
        slist.append(num**2)
    else: pass

if len(slist) == 0: print(-1)
else:
    print(sum(slist))
    print(slist[0])
