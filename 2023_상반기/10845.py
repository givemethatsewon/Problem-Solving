import sys

class Queue:
    def __init__(self):
        self.container = list()
        self.d_size = 0
    
    def empty(self):
        if not self.container:
            return 1
        return 0
    
    def push(self,data):
        self.container.append(data)
        self.d_size += 1
    
    def pop(self):
        if self.empty():
            return -1
        self.d_size -= 1
        return self.container.pop(0)
    
    def size(self):
        return self.d_size
    
    def front(self):
        if self.empty():
            return -1
        return self.container[0]
    
    def back(self):
        if self.empty():
            return -1
        return self.container[-1]

q = Queue()
n = int(sys.stdin.readline())

for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if 'push' in order:
        data = order.split()[-1]
        q.push(data)

    elif order == 'pop':
        print(q.pop())

    elif order == 'size':
        print(q.size())

    elif order == 'front':
        print(q.front())

    elif order == 'back':
        print(q.back())

    elif order == 'empty':
        print(q.empty())
