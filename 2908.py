a,b = map(str, input().split())

ra = int(a[::-1])
rb = int(b[::-1])
print(max(ra,rb))