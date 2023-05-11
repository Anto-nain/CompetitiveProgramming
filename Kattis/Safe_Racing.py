


def calcul(L,S):
    co = 0
    for c in range(2**L):
        config = bin(c)[2:]
        config = (L - len(config)) * '0' + config
        config += config
        if not S * '0' in config:
            co += 1
    return co
'''
for L in range(1,15):
    ligne = []

    for S in range(1,L + 1):
        s = str(calcul(L,S))
        ligne.append(' '*(8-len(s))+s)
    while len(ligne)<15:
        ligne.append(ligne[-1])
    print(ligne)

'''
L,S = map(int,input().split())
W = 123456789

res = 0

liste = [1]

for i in range(2,L+1):
    if i<=S:
        liste.append((liste[-1]*2+1)%W)
    else:
        sum = 0
        for u in range(S):
            sum+=liste[-1-u]
        liste.append(sum%W)
print(liste[-1])
