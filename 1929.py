def seive(x):
    if x == 0:
        return []
    prime = [True] * (x+1)
    prime[0] = prime[1] = False
    #x보다 작은 수 중에서 x의 약수는 전부 루트x보다 작거나 같다.
    for i in range(2,int(x**0.5)+1):
        if prime[i]:    #i가 소수이면
            #i의 배수들은 전부 소수가 아니므로 False로 바꿔주자
            for j in range(i**2,x+1,i):
                prime[j] = False
    return [i for i in range(x+1) if prime[i]]

m,n = map(int, input().split())
m_set = set(seive(m-1))
n_set = set(seive(n))
result = list(n_set - m_set)
result.sort()
print(*result, sep='\n')