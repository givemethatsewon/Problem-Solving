S = int(input())

cnt = 1
while True:
    S -= cnt
    cnt += 1
    if S <= 0:
        break

if S < 0:
    print(cnt - 2)
else:
    print(cnt - 1)
