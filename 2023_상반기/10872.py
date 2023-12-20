def factorial(n):
    if n == 0:  #base case
        result = 1
    else:   #factorial(n-1)타고 다시 돌아옴
        result = n*factorial(n-1)
    return result

if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
