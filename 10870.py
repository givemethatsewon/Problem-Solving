def pbn(n):
    if n == 0: result = 0
    elif n == 1: result = 1
    else:
        result = pbn(n-1) + pbn(n-2)
    return result

if __name__ == '__main__':
    n = int(input())
    print(pbn(n))
