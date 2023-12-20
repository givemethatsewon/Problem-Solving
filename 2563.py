#도화지 생성
paper = [[0]*100 for i in range(100)]

#해당되는 부분 칠하기
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[a + i][b + j] = 1

#전체 넓이 구하기
dot_sum = 0
for row in paper:
    dot_sum += sum(row)
print(dot_sum)