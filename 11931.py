import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort(reverse=True)

print(*nums, sep='\n')
