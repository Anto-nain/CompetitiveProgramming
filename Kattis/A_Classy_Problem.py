T = int(input())

def avant_alpha(ref,comp):
    L_ref = list(map(ord,[c for c in ref]))
    L_comp = list(map(ord,[c for c in comp]))
    if len(L_comp) > len(L_ref):
        res = False
    else:
        res = True
    try:
        ref = L_ref[0]
        comp = L_comp[0]
        i = 0
        while ref == comp:
            i += 1
            ref = L_ref[i]
            comp = L_comp[i]
        if ref < comp:
            return False
        else:
            return True
    except:
        return res
            
    
    

for t in range(T):
    n = int(input())
    D = {}
    
    for i in range(n):
        l = input().split(': ')
        D[l[0]] = l[1]

    classes = 0
    for e in D:
        D[e] = D[e].split('-')
        D[e][-1] = D[e][-1].split(' ')[0]
        classes = max(classes,len(D[e]))
    
    tri = []
    
    for e in D:
        D[e] = ['middle']*(classes-len(D[e])) + D[e]
        D[e] = D[e][::-1]
        valeur = ''
        for c in D[e]:
            if c == 'upper':
                valeur = valeur + '2'
            elif c == 'middle':
                valeur = valeur + '1'
            else:
                valeur = valeur + '0'
        D[e] = int(valeur)
        
        tri.append(e)
    
    for i in range(0,n):
        comparaison = tri[i]
        for j in range(0,i,-1):
            if D[tri[j]] > comparaison:
                tri[j+1],tri[j] = tri[j],tri[j+1]
            elif D[tri[j]] == comparaison:
                if avant_alpha(tri[j+1],tri[j]):
                    tri[j+1],tri[j] = tri[j],tri[j+1]
            else:
                break
    
    for i in range(n):
        for j in range(0, n-i-1):
            if D[tri[j]] > D[tri[j+1]] :
                tri[j], tri[j+1] = tri[j+1], tri[j]
            elif D[tri[j]] == D[tri[j+1]] and avant_alpha(tri[j+1],tri[j]):
                tri[j], tri[j+1] = tri[j+1], tri[j]
                
    tri = tri[::-1]
    
    for i in range(n):
        print(tri[i])
    print(30*'=')

                    
    
    
    