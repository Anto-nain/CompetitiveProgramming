t = []

while True :
    try :
        t.append(input())
    except :
        break


[n,m] = map(int,t[0].split(' '))
pages = list(map(int,t[1].split(' ')))
couples = []
for i in range(m):
    couples.append(list(map(int,t[i+2].split(' '))))



concept=list(range(1,n+1))
prereq=[couples[0][0]]
r=couples[0][0]
for j in range(1,m):
    if r!=couples[j][0]:
        r=couples[j][0]
        prereq.append(r)


for j in range(len(prereq)):
    j=len(prereq)-j-1
    concept.pop(prereq[j]-1)

arbre = dict()

for i in range(n):
    arbre[i+1]=[pages[i],None,True]

for i in range(m):
    arbre[couples[i][1]][1]=couples[i][0]



def page_couple(a,b,arbre):
    p=arbre[a][0]
    arbre[a][2]=False
    while arbre[a][1]!=None:
        a=arbre[a][1]
        p+=arbre[a][0]
        arbre[a][2]=False
        
    p+=arbre[b][0]
          
    while arbre[b][1]!=None and arbre[arbre[b][1]][2]==True:
        b=arbre[b][1]
        p+=arbre[b][0]
    return p

p_min=page_couple(concept[0],concept[1],arbre.copy())
for a in range(0,len(concept)-1):
    for b in range(a+1,len(concept)):
        p_min=min(p_min,page_couple(concept[a],concept[b],arbre.copy()))

print(p_min)
    

        