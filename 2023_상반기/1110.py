n = firstn = int(input())
nextn = -1
cnt = 0

while firstn != nextn:
    n1 = n%10
    n2 = (n//10 + n%10)%10
    nextn = 10*n1 + n2
    n = nextn
    cnt += 1

print(cnt)

