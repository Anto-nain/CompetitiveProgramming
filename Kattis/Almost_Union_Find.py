global rep
global parent
global rang
global sum
global nb

def find(p):
    p = rep[p]
    while parent[p] != p:
        p = parent[p]
    return p

def union(p,q):
    rp = find(p)
    rq = find(q)
    if rp != rq:
        if rang[rp] > rang[rq]:
            parent[rq] = rp
            sum[rp] += sum[rq]
            nb[rp] += nb[rq]
        else:
            parent[rp] = rq
            rang[rq] = max(rang[rq],rang[rp]+1)
            sum[rq] += sum[rp]
            nb[rq] += nb[rp]
       
def move(p,q):
    rp = find(p)
    rq = find(q)
    sum[rp] -= p
    nb[rp] -= 1
    
    rep[p] = rq
    sum[rq] += p
    nb[rq] += 1
    rang[rq] = max(2,rang[rq])
    
    
    
    
    '''
    i = len(parent)
    parent.append(i)
    
    rp = find(p)
    sum[rp] -= p
    nb[rp] -= 1
    
    rep[p] = i
    
    rep.append(i)
    rang.append(1)
    sum.append(p)
    nb.append(1)
    union(q, i)
    '''   

def aff(p):
    print(str(nb[find(p)])+' '+str(sum[find(p)]))

while True:
    try:
        n, m = map(int,input().split())
    except:
        break
    parent = list(range(n+1))
    rep = list(range(n+1))
    rang = [1 for _ in range(n+1)]
    sum = list(range(n+1))
    nb = [1 for _ in range(n+1)]
    
    for _ in range(m):
        t = list(map(int,input().split()))
        if t[0] == 1:
            union(t[1],t[2])
        elif t[0] == 2:
            move(t[1],t[2])
        else:
            aff(t[1])