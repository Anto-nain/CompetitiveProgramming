
'''
[N,M] = list(map(int,input().split(' ')))
class UF:
    def __init__(self,i):
        self.id = i
        self.parent = self
        self.rang = 1
        
    def find(self):
        if self.parent == self :
            return self
        else:
            return self.parent.find()
        
    def union(self,x):
        self_racine = self.find()
        x_racine = x.find()
        if x_racine.rang > self_racine.rang:
            self_racine.parent = x_racine
            x_racine.rang = max(x_racine.rang,self.racine.rang + 1)
        else:
            x_racine.parent = self_racine
            self_racine.rang = max(x_racine.rang + 1,self_racine.rang)
             
    def linked(self,x):
        return self.parent == x.parent


ponts = {}
for i in range(M):
    [a,b] = list(map(int,input().split(' ')))
    if a not in ponts:
        ponts[a] = UF(a)
    if b not in ponts:
        ponts[b] = UF(b)
    ponts[a].union(ponts[b])

racine = ponts[a].find()
ok = True
for i in ponts:
    #print(racine.id,ponts[i].find().id)
    if not ponts[i].linked(racine):
        ok = False

if ok:
    print('YES')
else:
    print('NO')
'''
ref = set()
N,M = list(map(int,input().split(' ')))
D = {}
for i in range(M):
    a,b = map(int,input().split(' '))
    ref.add(a)
    ref.add(b)

    if a in D:
        D[a].add(b)
    else:
        D[a] = set()
        D[a].add(b)
    if b in D:
        D[b].add(a)
    else:
        D[b] = set()
        D[b].add(a)
#print(D)
#print(ref)

soluce = set()


def parcours(i):
    soluce.add(i)
    #print(D)
    if i in D:
        s = {e for e in D[i]}
        del D[i]
        for k in s:
            parcours(k)
parcours(1)
#print(soluce)
if len(soluce) == N:
    print('YES')
else:
    print('NO')