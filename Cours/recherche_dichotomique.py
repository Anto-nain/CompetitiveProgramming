def recherche_dicho(L,x): #L trié on cherche l'indice auquel placer x tel que ce soit croissant
    maxi = len(L)
    mini = 0
    nb=0
    while True:
        nb+=1
        pos = int((maxi+mini)/2)
        #print(pos)
        if pos == 0:
            if L[pos] >= x:
                return 0
            else:
                return 1
        elif pos == len(L) - 1:
            if L[pos] <= x:
                return len(L)
            else:
                return len(L)-1
        else:
            if L[pos] <= x <= L[pos+1]:
                return pos+1
            elif L[pos] <= x:
                mini = pos
            else:
                maxi = pos


 