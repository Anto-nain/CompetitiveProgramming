n = int(input())


global D
D = dict()

def find(x):
    while D[x][0] != None:
        x = D[x][0]
        #print(x)
    return x

def union(x,y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        print(D[rx][1])
    else:
        if D[rx][1] > D[ry][1]:
            D[ry][0] = rx
            D[rx][1] += D[ry][1]
            print(D[rx][1])
        else:
            D[rx][0] = ry
            D[ry][1] += D[rx][1]
            print(D[ry][1])
    
    
while True:
    try:
        a,b = input().split()
    except:
        break
    #print(t,L)
    if a not in D:
        D[a] = [None,1]
    if b not in D:
        D[b] = [None,1]
    union(a,b)
        
    