from collections import deque

n = int(input())
if n == 1:
    print(1)
    exit(0)
    
cards = deque([i for i in range(n,0,-1)])

while True:
    cards.pop()
    if len(cards)  == 1:
        break
    else:
        x = cards.pop()
        cards.appendleft(x)

print(cards[0])