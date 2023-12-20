import sys

while True:
    a = input()
    stack = []
    
    if a == '.':
        break
    
    for i in a:
        if i == '(' or i =='[':
            stack.append(i)
        
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop() #Â¦ ¸ÂÀ¸¸é ¹Ù·Î stack ºñ¿öÁÜ
            else:
                stack.append(']')
                break
        
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop() #Â¦ ¸ÂÀ¸¸é ¹Ù·Î ºñ¿öÁÜ
            else:
                stack.append(')')  
                break
            
    if len(stack) == 0:
        print('yes')
    else:
        print('no')