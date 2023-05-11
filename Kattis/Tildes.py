n,q = map(int,input().split())

global L
L = [[None,1] for i in range(n+1)]

def find(x):
    while L[x][0] != None:
        x = L[x][0]
        #print(x)
    return x

def union(x,y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    else:
        if L[rx][1] > L[ry][1]:
            L[ry][0] = rx
            L[rx][1] += L[ry][1]
        else:
            L[rx][0] = ry
            L[ry][1] += L[rx][1]
    

    


for i in range(q):
    t = input().split()
    #print(t,L)
    if t[0] == 't':
        a,b = int(t[1]),int(t[2])
        union(a,b)
    else :
        a = int(t[1])
        print(L[find(a)][1])
        
    