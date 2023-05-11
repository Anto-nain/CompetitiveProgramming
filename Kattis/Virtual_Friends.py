class UF:
    def __init__(self,i):
        self.id = i
        self.parent = self
        self.rang = 1
        self.nb = 1
        
    def find(self):
        if self.parent == self :
            return self
        else:
            return (self.parent).find()
    
    def linked(self,x):
        return self.parent == x.parent
        
    def union(self,x):
        self_racine = self.find()
        x_racine = x.find()
        if self_racine != x_racine:
            if x_racine.rang > self_racine.rang:
                self_racine.parent = x_racine
                x_racine.rang = max(x_racine.rang,self_racine.rang + 1)
                x_racine.nb += self_racine.nb
                print(x_racine.nb)
            else:
                x_racine.parent = self_racine
                self_racine.rang = max(x_racine.rang + 1,self_racine.rang)
                self_racine.nb += x_racine.nb
                print(self_racine.nb)
        else:
            print(self_racine.nb)

N = int(input())
for i in range(N):
    D = {}
    for j in range(int(input())):
        [noms1,noms2] = input().split(' ')
        if noms1 not in D:
            D[noms1] = UF(noms1)
        if noms2 not in D:
            D[noms2] = UF(noms2)
        D[noms1].union(D[noms2])
    
