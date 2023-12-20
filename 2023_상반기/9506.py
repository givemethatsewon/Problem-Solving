import sys

while True:
    n = int(input())
    if n == -1: sys.exit()
    n_list = []
    for i in range(1,n):
        if n%i == 0: n_list.append(i)

    if sum(n_list) == n:
        del n_list[0]
        print(n,'=',1,end=' ')
        for j in n_list:
            print('+',j,end=' ')
        print()

    else:
        print(n,'is NOT perfect.')