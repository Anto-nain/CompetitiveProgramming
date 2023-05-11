T = int(input())

for t in range(T):
    tag = "Case #"+str(t+1)+': '
    
    N = int(input())
    
    L = input().split()
    set_vue = set()
    tot = []
    ok = True
    
    for i in range(len(L)):
        if L[i] not in set_vue:
            set_vue.add(L[i])
            tot.append(L[i])
        else:
            if L[i-1] != L[i]:
                ok = False
                break
            
    
    if not ok:
        print(tag+'IMPOSSIBLE')
    else:
        print(tag +' '.join(tot))