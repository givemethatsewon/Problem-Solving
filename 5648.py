import sys
input = sys.stdin.readline

before = []
after = []
cnt = 0

first = input().split()
for i in range(len(first)):
    if i == 0:
        n = int(first[i])
    else:
        before.append(first[i])
        cnt += 1
        
while cnt < n:
    line = input().split()   #문자열로 받기
    cnt += len(line)
    for num in line:
        before.append(num)

for num in before:
    rev = int(num[::-1])
    after.append(rev)

after.sort()
print(*after, sep='\n')    
