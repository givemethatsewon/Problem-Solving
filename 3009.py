x_list = []
y_list = []
for i in range(3):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)


for i in range(3):
    if x_list.count(x_list[i]) == 2:
        key_x = x_list[i]
    if y_list.count(y_list[i]) == 2:
        key_y = y_list[i]
        
if key_x in x_list: del x_list[x_list.index(key_x)]
if key_y in y_list: del y_list[y_list.index(key_y)]

target_x = sum(x_list)-key_x
target_y = sum(y_list)-key_y

print(target_x,target_y)