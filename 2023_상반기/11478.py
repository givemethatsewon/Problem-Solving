s = input()
part = set()
length = len(s)

for i in range(1, length+1):
    j = 0
    while j + i <= length:
        part.add(s[j:j+i])
        j += 1
    
print(len(part))