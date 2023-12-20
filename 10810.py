n, m = map(int, input().split())
box = [0] * n   #n개의 바구니 형성

for turn in range(m):   #m번 시행
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    box = box[:i] + [k] * (j - i + 1) + box[j + 1:]
print(*box, sep=' ')