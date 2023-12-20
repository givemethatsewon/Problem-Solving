import sys

nums = []
op = []

while True:
    nums.append(int(input()))
    operator = input()
    if operator == '=':
        break
    else:
        op.append(operator)
        
result = nums[0]
for i in range(len(op)):
    if op[i] == '+':
        result += nums[i+1]
    elif op[i] == '-':
        result -= nums[i+1]
    elif op[i] == '*':
        result *= nums[i+1]
    elif op[i] == '/':
        result /= nums[i+1]
        result = int(result)
print(result)