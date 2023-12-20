n = int(input())
vote = input()
A_cnt = 0
B_cnt = 0

for v in vote:
    if v == 'A': A_cnt += 1
    else: B_cnt += 1

if A_cnt > B_cnt: print('A')
elif A_cnt < B_cnt: print('B')
else: print('Tie')
