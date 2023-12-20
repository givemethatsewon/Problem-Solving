n, m = map(int, input().split())

num_list = list(range(1,n+1))   #[1,2,3,...,n]
for turn in range(m):    #m번 교체
    i,j = map(int, input().split())
    i -= 1
    j -= 1
    i_data = num_list[i]    #i의 요소 확인
    j_data = num_list[j]    #j의 요소 확인
    del num_list[i] #i번째 요소 삭제
    num_list.insert(i,j_data)   #i번째에 j_data 삽입
    del num_list[j] #j번째 요소 삭제
    num_list.insert(j,i_data)   #j번째에 i_data 삽입
print(*num_list, sep=' ')