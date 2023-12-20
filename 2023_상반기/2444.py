k = int(input())
series_1 = list(range(1,k))
series_2 = list(range(k,0,-1))

series = series_1 + series_2

for n in series:
    print(' '*(k-n), '*'*(2*n-1), sep='')