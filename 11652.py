import sys
input = sys.stdin.readline

n = int(input())
cards = dict()

for i in range(n):
    num = int(input())
    try:
        cards[num] += 1
    except:
        cards[num] = 1

#key 리스트
k = list(cards.keys())
#value 리스트
v = list(cards.values())
target = max(v)

candidate = []
for key in k:
    if cards[key] == target:
        candidate.append(key)

print(min(candidate))
