N = int(input())
for i in range(N):
    G = int(input())
    L = list(map(int,input().split(' ')))
    s = set()
    for e in L:
        if e in s:
            s.remove(e)
        else:
            s.add(e)
    print('Case #'+str(i+1)+': '+str(s)[1:-1])
    
        