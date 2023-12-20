r_list = []

def to_bin(n):
    if n == 1:
        r_list.append(1)
        return
    r = n % 2
    r_list.append(r)
    q = n // 2
    return to_bin(q)

if __name__ == '__main__':
    n = int(input())
    to_bin(n)
    for num in list(reversed(r_list)):
        print(num, end='')