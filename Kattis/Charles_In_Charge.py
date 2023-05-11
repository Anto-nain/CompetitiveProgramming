N,M,X = map(int,input().split())

graph = (N+1)*[None]

for i in range(M):
    C1,C2,T = map(int,input().split())
    
    if graph[C1] == None:
        graph[C1] = {C2:T,"chemins" : dict()} #dict[longueur de l'origine] = [max(int),chemin(liste)]
    else:
        graph[C1][C2] = T
    
    if graph[C2] == None:
        graph[C2] = {C1:T,"chemins" : [],"distances" : [], "maxs" : []}
    else:
        graph[C2][C1] = T
    