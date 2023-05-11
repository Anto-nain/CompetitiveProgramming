from math import log

n = int(input())


            
def premier(n):
    if n<=1:
        return False
    for k in range(2,int(n**0.5)+1):
        if not n%k:
            return False
    return True

if premier(n):
    print('yes')
else:

    oui=False

    

                
    delta = 1e-10
    for p in range(int(n**0.5+1)):
        if premier(p):
            x = log(n)/log(p)
            if abs(int(x)-x) < delta:
                oui = True

    if oui :print('yes')
    else:print('no')
                
                
