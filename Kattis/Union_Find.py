import sys
'''
import time
t1 = time.time()

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
        self_nb = self.nb
        x_nb = x.nb
        if self_racine != x_racine:
            if x_racine.rang > self_racine.rang:
                self_racine.parent = x_racine
                x_racine.rang = max(x_racine.rang,self_racine.rang + 1)
                x_racine.nb = x_nb+self_nb
            elif x_racine.rang < self_racine.rang:
                x_racine.parent = self_racine
                self_racine.rang = max(x_racine.rang + 1,self_racine.rang)
                self_racine.nb = x_nb+self_nb
            else:
                if x_nb > self_nb:
                    self_racine.parent = x_racine
                    x_racine.rang = max(x_racine.rang,self_racine.rang + 1)
                    x_racine.nb = x_nb+self_nb
                else:
                    x_racine.parent = self_racine
                    self_racine.rang = max(x_racine.rang + 1,self_racine.rang)
                    self_racine.nb = x_nb+self_nb
             


t = sys.stdin.read().splitlines()

[N,Q] = list(map(int,t[0].split(' ')))
D = {}
for i in range(Q):
    #print(t[i+1])
    [s,a,b] = t[i+1].split(' ')
    if a not in D:
        D[a] = UF(a)
    if b not in D:
        D[b] = UF(b)
    if s == '=':
        D[a].union(D[b])
    else:
        if D[a].linked(D[b]):
            sys.stdout.write('yes\n')
        else:
            sys.stdout.write('no\n')

t2 = time.time()
print(t2-t1)
'''
global D
D = {}

def find(i):
    #print(i,D[i]['parent'])
    while parents[i] != i:
        i=parents[i]
    return i
    

def union(a,b):
    #print(D,a,b,find(a),find(b))
    a_racine = find(a)
    b_racine = find(b)
    a_racine_rang = rangs[a_racine]
    b_racine_rang = rangs[b_racine]
    #print(a,D[a_racine]['rang'],b,D[b_racine]['rang'])
    if a_racine != b_racine:
        if b_racine_rang > a_racine_rang:
            parents[a_racine] = b_racine
            rangs[b_racine] = max(b_racine_rang,a_racine_rang + 1)
            #b_racine.nb = b_nb+a_nb
        else: #b_racine_rang < a_racine_rang:
            parents[b_racine] = a_racine
            rangs[a_racine] = max(b_racine_rang + 1,a_racine_rang)
            #a_racine.nb = b_nb+a_nb
    #print(a,D[a_racine]['rang'],b,D[b_racine]['rang'])
        #else:
            #if b_nb > a_nb:
                #a_racine.parent = b_racine
                #b_racine.rang = max(b_racine.rang,a_racine.rang + 1)
                #b_racine.nb = b_nb+a_nb
            #else:
                #b_racine.parent = a_racine
                #a_racine.rang = max(b_racine.rang + 1,a_racine.rang)
                #a_racine.nb = b_nb+a_nb
def linked(a,b):
    #print(D,a,b)
    aa = find(a)
    bb = find(b)
    #print(aa,bb)
    if aa == bb:
        return True
    else:
        return False

t = sys.stdin.read().splitlines()
N,Q = list(map(int,t[0].split(' ')))

parents=list(range(0,N+1))
rangs=[1]*(N+1)



for i in range(Q):
    #print(t[i+1])
    [s,a,b] = t[i+1].split(' ')
    a=int(a)
    b=int(b)    
    if s == '=':
        union(a,b)
    else:
        if linked(a,b):
            sys.stdout.write('yes\n')
        else:
            sys.stdout.write('no\n')