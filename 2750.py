n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()
print(*nums, sep='\n')