ans = [1, 1, 2, 2, 2, 8]
user = list(map(int, input().split()))
checked = []

for i in range(6):
    data = ans[i] - user[i]
    checked.append(data)
print(*checked, sep=' ')