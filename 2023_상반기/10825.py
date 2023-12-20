import sys
input = sys.stdin.readline

scores = []
n = int(input())

for _ in range(n):
    personel = input().split()  
    for i in range(1,4):
        personel[i] = int(personel[i])
    scores.append(personel)


scores.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for personel in scores:
    print(personel[0])