n = input()
nums = [int(i) for i in n]
nums.sort(reverse=True)

print(*nums, sep='')