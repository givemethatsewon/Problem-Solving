#리스트 형태로 입력 저장
user = list(map(int, input().split()))
#정답 저장
n_list = [i for i in range(1,9)]
r_list = n_list[::-1]
#출력
if user == n_list: print('ascending')
elif user == r_list: print('descending')
else: print('mixed')

