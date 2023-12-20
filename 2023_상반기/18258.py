import sys

class CQueue:
    def __init__(self, k:int):
        MAXSIZE = k
        self.container = [None for _ in range(MAXSIZE + 1)]
        self.head = 0
        self.tail = 0
    
    def empty(self):
        if self.head == self.tail:
            return 1
        return 0
    
    def enqueue(self, data):
        self.container[self.tail] = data
        self.tail += 1
        
    def dequeue(self): 
        if self.empty():
            return -1
        ret = self.container[self.head]
        self.head += 1
        return ret
    
    def size(self):
        return self.tail - self.head
    
    def front(self):
        if self.empty():
            return -1
        return self.container[self.head]
    
    def back(self):
        if self.empty():
            return -1
        return self.container[self.tail-1]
    
n = int(sys.stdin.readline())
q = CQueue(n)

for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if 'push' in order:
        data = order.split()[-1]
        q.enqueue(data)

    elif order == 'pop':
        print(q.dequeue())

    elif order == 'size':
        print(q.size())

    elif order == 'front':
        print(q.front())

    elif order == 'back':
        print(q.back())

    elif order == 'empty':
        print(q.empty())
