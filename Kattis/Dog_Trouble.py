from functools import lru_cache
import itertools
import numpy as np

[N,M] = map(int,input().split(' '))
Mat = np.zeros([N,M])

for i in range(N):
    Mat[i,:] = list(map(int,input().split(' ')))

def max_ligne(L):
    indice = 0
    max = L[0]
    for i in range(1,len(L)):
        if L[i] > max:
            indice = i
            max = L[i]
    return [int(indice),int(max)]


t=np.max(Mat)
'''
ordre = list(range(N)) 
cas = list(itertools.permutations(ordre))

T=[]

for i in range(len(cas)):
    Matrice=Mat.copy()
    T.append(t*N)
    for j in range(N):
        L=list(Matrice[cas[i][j],:])
        [indice,ti] = max_ligne(L)
        Matrice[:,indice] = N*[-np.inf]
        T[i]-=ti

print(int(min(T)))
'''
cas = []

class arbre:
    def __init__(self,matrice_initiale,T,indices_suivants):
        self.matrice = np.copy(matrice_initiale)
        self.T = T
        self.suivants = list(np.copy(indices_suivants))
        
        if self.suivants == []:
            cas.append(T)
        
        else : 
            for i in range(len(self.suivants)):
                [j,ti] = max_ligne(list(self.matrice[self.suivants[i],:]))
                matrice = np.copy(self.matrice)
                matrice[:,j] = N*[-np.inf]
                suivants = list(np.copy(self.suivants))
                suivants.pop(i)
                
                arbre(matrice,self.T-ti,suivants)
arbre(Mat,t*N,list(range(N)))

print(int(min(cas)))
        