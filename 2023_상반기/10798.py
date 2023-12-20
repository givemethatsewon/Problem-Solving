table = []
for _ in range(5):
    inner = input()
    table.append([i for i in inner])
    
cnt = [len(row) for row in table]
max_cnt = max(cnt)

for row in table:
    while len(row) < max_cnt:
        row.append('')
   
ans = ''
for i in range(max_cnt):
    for row in table:
        ans += row[i]

print(ans)