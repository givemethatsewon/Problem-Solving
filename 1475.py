room = [int(i) for i in input()]
cnt_list = [0 for _ in range(10)]

for n in room:
    cnt_list[n] += 1

mini = min(cnt_list[6], cnt_list[9])
maxi = max(cnt_list[6], cnt_list[9])
process = maxi - mini

if process % 2 == 0:
    result = mini + process // 2
else:
    result = mini + process // 2 + 1
    
cnt_list[6] = cnt_list[9] = result

print(max(cnt_list))

