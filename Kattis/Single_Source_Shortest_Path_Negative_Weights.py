def Dijkstra(link,start):#return arbre min distance pondérée
    pass
    

while True:
    try:
        n,m,q,s = map(int,input().split())
    except:
        break
    
    link = {}
    for _ in range(m):
        u,v,w = map(int,input().split())
        
        if u not in link:
            link[u] = {v:w}
        else:
            link[u][v] = w
        if v not in link:
            link[v] = {u:w}
        else:
            link[v][u] = w
        
    
        
        
            