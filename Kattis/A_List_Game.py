from functools import lru_cache
from math import sqrt
from signal import pause

t = input()

X = int(t)
borne = int(sqrt(X))+1

@lru_cache #permet de mémoriser les résultats obtnenus de la fonction afin de de ne pas la réexécuter et de gagner en rpidite (mais perdre ne mémoire)
def est_premier(n) :
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
        


#décompo facteurs premiers
k = 0
while borne != 1 :
    if X%borne == 0 and est_premier(borne) :
        k += 1
        X //= borne
    else :
        borne -= 1
        
if X == 1:
    print(1)
else :
    print(k)

