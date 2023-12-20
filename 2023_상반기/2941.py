sentence = input()
total = len(sentence)   #전체 글자 개수 계산
remainder = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for letter in remainder:
    cnt += sentence.count(letter)
    
if 'dz=' not in sentence:
    total = total - cnt
else:
    dzcnt = sentence.count('dz=')
    cnt = cnt + dzcnt
    total = total - cnt
print(total)