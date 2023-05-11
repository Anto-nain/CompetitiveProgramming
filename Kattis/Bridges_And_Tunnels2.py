N,m,p = map(int,input().split())



route = [None for _ in range(N)]
arbre = [None for _ in range(N)] #[racine,rang]
set_route = [None for _ in range(N)]
set_arbre = [None for _ in range(N)]
voisin = [set() for _ in range(N)]

def find(a):
    x=a 
    while arbre[x][0]!=x:
        x=arbre[x][0]
    return x

def union(a,b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if arbre[ra][1]>arbre[rb][1]:
        arbre[ra][1] += arbre[rb][1]
        arbre[rb][0] = ra
    else:
        arbre[rb][1] += arbre[ra][1]
        arbre[ra][0] = rb
        

for i in range(m):
    a,b,t,kind = input().split()
    a,b,t = map(int,(a,b,t))
    voisin[a].add(b)
    voisin[b].add(a)
    
    
    if set_route[a] == None:
        route[a] = [None for _ in range(N)]
        route[a][b] = {'I' : None, 'O' : None}
        route[a][b][kind] = t
        set_route[a] = 0
    elif route[a][b][kind] == None:
        route[a][b][kind] = t
    else:
        route[a][b][kind] = min(t,route[a][b][kind])
        
    if set_route[b] == None:
        route[b] = [None for _ in range(N)]
        route[b][a] = {'I' : None, 'O' : None}
        route[b][a][kind] = t
        set_route[b] = 0
    elif route[b][a][kind] == None:
        route[b][a][kind] = t
    else:
        route[b][a][kind] = min(t,route[b][a][kind])
        

    
    
    if set_arbre[a] == None:
        arbre[a] = [a,1]
    if set_arbre[b] == None:
        arbre[b] = [b,1]
    union(a,b)
      
    
        

for _ in range(p):
    a,b = map(int,input().split())
    if find(a) != find(b):
        print('IMPOSSIBLE')
    else:
        Temps=[None for k in range(N)] # [[T_outside,T_tot,numéro de branche]]
        #print(a,Temps)
        Temps[a]=[0,0]
        noeuds_a_traiter = {a}
        while True:
            noeuds_suivants = set()
            for n in noeuds_a_traiter:
                for enfant in voisin[n]:
                    #print(route)
                    #print(n,enfant)
                    tno = Temps[n][0]
                    tnt = Temps[n][1]
                    
                    incr_o = route[n][enfant]['O']
                    incr_i = route[n][enfant]['I'] 
                    
                    
                    if Temps[enfant] == None:
                        if incr_i == None:
                            Temps[enfant] = [tno+incr_o,tnt+incr_o]
                        else:
                            Temps[enfant]=[tno,tnt+incr_i]
                                         
                    else:
                        teo = Temps[enfant][0]
                        tet = Temps[enfant][1]
                        if incr_i == None:
                            if tno + incr_o < teo :
                                Temps[enfant] = [tno+incr_o,tnt+incr_o]
                                noeuds_suivants.add(enfant)
                            elif tno + incr_o == teo:
                                if tnt + incr_o < tet:
                                    Temps[enfant] = [tno+incr_o,tnt+incr_o]
                                    noeuds_suivants.add(enfant)
                        else:
                            if tno < teo:
                                Temps[enfant] = [tno,tnt+incr_i]
                                noeuds_suivants.add(enfant)
                            elif tno == teo:
                                if tnt + incr_i < tet:
                                    Temps[enfant] = [tno,tnt+incr_i]
                                    noeuds_suivants.add(enfant)
                               
            noeuds_a_traiter = noeuds_suivants
            if len(noeuds_a_traiter) == 0:
                break
        if Temps[b]==None:
            Temps[b] = [None,None]
        if Temps[b][0] == None:
            Temps[b][0] = 0
        if Temps[b][1] == None:
            Temps[b][1] = 0
        print(str(Temps[b][0])+' '+str(Temps[b][1]))
