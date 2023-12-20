n = int(input())

line = 0    #몇 번째 줄인지
end = 0
while n > end:
    line += 1
    end += line

gap = end - n   #해당 줄에서 index
if line % 2 == 0:
    up = line - gap
    down = 1 + gap
else:
    up = 1 + gap
    down = line - gap
    
print(f'{up}/{down}')
