s = input()
length = len(s)

suffix = []
for i in range(length):
    suffix.append(s[i:])

suffix.sort()
print(*suffix, sep='\n')