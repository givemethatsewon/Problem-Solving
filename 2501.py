n,k = map(int, input().split())
start = 1
factors = []

while start <= n:
    if n % start == 0:
        factors.append(start)
    start += 1

if len(factors) >= k:
    print(factors[k-1])
else:
    print(0)