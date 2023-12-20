N = int(input())
abc_list = []
reward_list = []

for i in range(N):
    a,b,c = map(int,input().split())
    abc_list.append([a,b,c])
    abc_cnt = len(set(abc_list[i]))
    
    if abc_cnt == 1:
        reward = 10000 + 1000*abc_list[i][0]
    elif abc_cnt == 3:
        reward = 100*max(abc_list[i])
    else:
        for j in range(3):
            if abc_list[i].count(abc_list[i][j]) == 2:
                reward = 1000 + 100*abc_list[i][j]
                
    reward_list.append(reward)

print(max(reward_list))
