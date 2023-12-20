t = int(input())    #테스트 케이스 받음

r_list = []
s_list = []
for i in range(t):
    r,s = input().split()   #반복횟수, 반복할 문자
    s = [s[i] for i in range(len(s))]   #문자열 분리
    r_list.append(r)
    s_list.append(s)

for i in range(len(s_list)):
    for j in range(len(s_list[i])):
        print(s_list[i][j]*int(r_list[i]),end='')
    print()
