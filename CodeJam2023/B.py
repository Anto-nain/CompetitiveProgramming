T = int(input())

for t in range(T):
    tag = "Case #"+str(t+1)+':' + ' '
    
    M,R,N = map(int,input().split())
    liste_lamp = [-R] + list(map(int,input().split())) + [M+R]
    
    ok = True
    
    for i in range(1,len(liste_lamp)):
        if liste_lamp[i]-liste_lamp[i-1] > 2*R:
            ok = False
            break
    
    if not ok:
        print(tag + "IMPOSSIBLE")
    else:
        iref = 0
        xref = liste_lamp[0]
        nb = 0
        for i in range(1,len(liste_lamp)):
            x = liste_lamp[i]
            if x-xref > 2*R:
                nb += 1
                iref = i-1
                xref = liste_lamp[iref]
        print(tag + str(nb))