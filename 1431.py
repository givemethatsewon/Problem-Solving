import sys
input = sys.stdin.readline

processed = []
#시리얼 번호 입력 및 후처리
n = int(input())
for _ in range(n):
    #시리얼번호 자체
    serial = input().rstrip()
    #길이
    length = len(serial)
    #숫자들의 합
    total = 0
    for i in serial:
        try:
            total += int(i)
        except ValueError:
            pass
    #후처리 리스트에 리스트 형태로 추가
    processed.append([length, total, serial])

processed.sort(key = lambda x : (x[0], x[1], x[2]))

for serial in processed:
    print(serial[2])