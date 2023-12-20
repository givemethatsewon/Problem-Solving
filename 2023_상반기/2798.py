from itertools import combinations
import sys
#입력
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
#알고리즘
combi_list = list(combinations(cards,3))    #조합 결과 저장
total_list = list(map(sum, combi_list))     #조합의 합 결과 저장
differ_list = []    #조합의 합과 m값의 차이 저장할 예정

#0보다 큰 경우에만 idx 맞춰서 total 출력
for total in total_list:
    differ = m - total
    if differ < 0: differ_list.append(m)
    else: differ_list.append(m-total)

idx = differ_list.index(min(differ_list))
print(total_list[idx])
        
