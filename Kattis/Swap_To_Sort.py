N,K = map(int,input().split())
global L
L = [[None,1] for i in range(N+1)]

def find(x):
    while L[x][0] != None:
        x = L[x][0]
    return x

def union(x,y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    else:
        if L[rx][1] > L[ry][1]:
            L[ry][0] = rx
            L[rx][1] = max(L[rx][1],L[ry][1]+1)
        else:
            L[rx][0] = ry
            L[ry][1] = max(L[ry][1],L[rx][1]+1)

for i in range(K):
    a,b = map(int,input().split())
    
    union(a,b)

non = False
for i in range(1,(N+1)//2):
    if find(i) != find(N-i+1):
        non = True
        break

if non:
    print('No')
else:
    print('Yes')
    