n = int(input())
linelist = []
for i in range(n):
    line = input()
    linelist.append(line)
    line = 0                                        

linelist2 = []
linelist3 = []
for i in range(n):
    for j in range(n):
        data = linelist[j][i]
        linelist2.append(data)
    s = ''.join(linelist2)
    linelist3.append(s)
    linelist2 = []

wid=0
ver=0

for i in range(n):
    for j in range(2,n+1):
        test1 = linelist[i].split('X')
        cnt = test1.count('.'*j)
        wid +=  cnt
        test1 = linelist3[i].split('X')
        cnt = test1.count('.'*j)
        ver +=  cnt
        
print(wid, ver)