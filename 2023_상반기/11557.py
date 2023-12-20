testCase = int(input())
rank_univ = []
rank_alco = []
winner = []

for i in range(testCase):
    univNum = int(input())
    rank_univ = []
    rank_alco = []
    for i in range(univNum):
        univ, alco =input().split()
        rank_univ.append(univ)
        rank_alco.append(int(alco))
        
    indexNum = rank_alco.index(max(rank_alco))
    winner.append(rank_univ[indexNum])

for i in range(len(winner)):
    print(winner[i])