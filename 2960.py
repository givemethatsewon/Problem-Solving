n,k = map(int, input().split())  #n보다 작거나 같은 수 중 k번째 지우는 수를 구해야함
cnt = 0

nums = [True] * (n+1)
nums[0] = nums[1] = False
breaker = False

for i in range(2, n+1):
    if nums[i]:
        for j in range(i, n+1, i):
            if nums[j] == False: 
                pass
            else:
                nums[j] = False
                ans = j
                cnt += 1
                
            if cnt == k:
                breaker = True
                break
    if breaker == True:
        break
print(ans)