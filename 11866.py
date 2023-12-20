from collections import deque

n, k = map(int, input().split())
array = deque([i for i in range(1, n+1)])
answer = deque()

#큐를 회전시키면서 answer에 k번째 숫자 넣기
while array:
    array.rotate(-k+1)
    x = array.popleft()
    answer.append(x)

#출력형식에 맞게 출력
a = ', '.join(map(str, answer))
print(f'<{a}>')
