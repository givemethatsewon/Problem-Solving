t = int(input())
y_sum = k_sum = 0

for i in range(t):
    for j in range(9):
        y, k = map(int, input().split())
        y_sum += y
        k_sum += k
    if y_sum > k_sum: print('Yonsei')
    elif y_sum < k_sum: print('Korea')
    else: print('Draw')