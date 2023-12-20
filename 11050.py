from itertools import combinations

n,k = map(int, input().split())

data = [i for i in range(n)]

combi = list(combinations(data, k))

print(len(combi))