import numpy as np
#n = int(input())
n = 50
m = n
it = 0

def func(jour,impr,sta):
    global m
    global n
    global it
    it += 1
    print(it,jour,impr,sta)
    if sta >= n:
        m = jour
    elif jour >= m:
        pass
    else:
        for i in range(min(n-sta,impr + 1)):
            func(jour + 1,2*impr - i,sta + i)
    
   
func(0,1,0) 
print(m)
