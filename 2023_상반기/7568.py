import sys
input = sys.stdin.readline

n = int(input())
p_list = [list(map(int, input().split())) for i in range(n)]
cnt_list = []   

for p in p_list:
    cnt = 0
    w = p[0]
    h = p[1]
    for p in p_list:
        w_prime = p[0]
        h_prime = p[1]
        if w < w_prime and h < h_prime:
            cnt += 1
    cnt_list.append(cnt + 1)
    
print(*cnt_list, sep=' ')