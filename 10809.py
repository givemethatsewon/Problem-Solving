#알파벳 리스트
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#단어 입력
s = input()
#단어에 있는지 하나씩 확인
for alphabet in alphabet_list:
    idx = s.find(alphabet)
    print(idx, end=' ')