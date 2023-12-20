#단어 입력받고 대문자로 통일
word = input().upper()
#중복을 제거한 리스트 생성
w_list = [i for i in word]
l_list = list(set(w_list))
#단어별 개수를 저장할 n_list 생성
n_list = [] #n_list와 l_list의 객체 순서 일치 확인해야함
for letter in l_list:
    n_list.append(w_list.count(letter))

max_idx = n_list.index(max(n_list))
if n_list.count(max(n_list)) == 1:
    print(l_list[max_idx])
else: print('?')

