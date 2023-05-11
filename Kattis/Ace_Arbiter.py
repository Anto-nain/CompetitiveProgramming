n = int(input())
scores = []
for i in range(n):
    scores.append(list(map(int,input().split('-'))))

serveur = 0
svg = None
ok = True

for i in range(n):
    score = scores[i]
    if svg != None:
        if svg == score:
            pass
    
    svg = score
    
    
    
    
    
    
    
    
    if sum(score)%2 == 1 or sum(score) == 0:
        if serveur == 0:
            serveur = 1
        else:
            serveur = 0
    
        
if ok:
    print('ok')
    
    