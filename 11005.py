#10진법 수 n, 바꿀 진법 b 입력 받기
n, b = map(int, input().split())

#나머지들 리스트에 담기
remain = []
while n != 0:
    r = n % b
    n = n // b
    remain.append(r)

#나머지들을 문자열로 바꿔줌 + 알파벳으로
pre = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
post = {v:k for k,v in pre.items()}

for i in range(len(remain)):
    remain[i] = post[remain[i]]

#거꾸로 출력
net = ''.join(remain[::-1])
print(net)
    