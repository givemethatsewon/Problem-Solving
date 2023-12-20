n = int(input())
vote_list = list(map(int, input().split()))
pro = 0
con = 0
neut = 0

for vote in vote_list:
    if vote == 1:
        pro += 1
    elif vote == -1:
        con += 1
    else:
        neut += 1

if neut >= n/2:
    print('INVALID')
else:
    if pro > con:
        print('APPROVED')
    else:
        print('REJECTED')