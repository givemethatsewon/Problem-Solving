import sys
input = sys.stdin.readline

t_case = int(input())
cents = [25, 10, 5, 1]

for _ in range(t_case):
    money = int(input())
    result = []
    for cent in cents:
        result.append(money // cent)
        money = money % cent
    print(*result, sep=' ')