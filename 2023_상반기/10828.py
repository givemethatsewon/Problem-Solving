import sys
input = sys.stdin.readline

class Stack():
    def __init__(self):
        self.container = list()
        self.d_size = 0
    
    def empty(self):
        if not self.container:
            return 1
        return 0
    
    def push(self, data):
        self.d_size += 1
        self.container.append(data)
        
    def pop(self):
        if self.empty():
            return -1
        self.d_size -= 1
        return self.container.pop()
    
    def top(self):
        if self.empty():
            return -1
        return self.container[-1]
    
    def size(self):
        return self.d_size

s = Stack()

n = int(input())
for i in range(n):
    order = input().strip()
    
    if 'push' in order:
        num = order.split()[1]
        s.push(num)
    elif order == 'pop':
        print(s.pop())
    elif order == 'size':
        print(s.size())
    elif order == 'empty':
        print(s.empty())
    elif order == 'top':
        print(s.top())
    