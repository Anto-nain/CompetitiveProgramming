n,m = map(int,input().split())
graph = dict()

impossible = False
top = set()
for i in range(m):
    a,b = map(int,input().split())
    if a not in graph:
        graph[a] = [set(),{b}]
        top.add(a)
    else:
        graph[a][1].add(b)    
    if b not in graph:
        graph[b] = [{a},set()]
    else:
        graph[b][0].add(a)
    if b in top:
        top.remove(b)

ordre = []

while len(top) != 0:
    new_top = set()
    for sommet in top:
        #print(top,graph)
        ordre.append(sommet)
        for enfant in graph[sommet][1]:
            if graph[enfant][0] == {sommet}:
                new_top.add(enfant)
            else:
                graph[enfant][0].remove(sommet)
    top = new_top

#print(ordre)

if len(ordre) == n:
    for i in ordre : print(i)
else:
    print('impossible')
    
    