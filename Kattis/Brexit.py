C,P,X,L = map(int,input().split())
link = dict()

for i in range(P):
    A,B = map(int,input().split())
    if A not in link:
        link[A] = [0,set()]
    if B not in link:
        link[B] = [0,set()]
    link[A][1].add(B)
    link[A][0]+=1
    link[B][1].add(A)
    link[B][0]+=1

#print(link)
leave = False

liste_to_remove = [L]

while len(liste_to_remove) != 0 :
    #print(liste_to_remove)
    retire = liste_to_remove.pop()
    s = {retire}
    for pays in link[retire][1]:
        #print(retire, link[pays][1])
        link[pays][1].remove(retire)
        #print(pays,link[pays][1],link[pays][0])
        if 2*len(link[pays][1]) <= link[pays][0] and pays not in s:
            liste_to_remove.append(pays)
            s.add(pays)
    if X in s:
        leave = True
        break

if leave:
    print("leave")
else:
    print("stay")

    
        