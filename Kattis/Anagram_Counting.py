from math import factorial


t = []

while True :
    try :
        t.append(input())
    except :
        break

L = []
for i in range(len(t)):
    L.append({})
    for lettre in t[i]:
        if lettre not in L[i]:
            L[i][lettre] = 1
        else :
            L[i][lettre] += 1


resultat = []
for i in range(len(L)):
    place = len(t[i])
    produit = 1
    for lettre in L[i]:
        produit *= factorial(place)//(factorial(L[i][lettre])*factorial(place-L[i][lettre]))
        place-=L[i][lettre]
    resultat.append(produit)

s = ''
for nombre in resultat :
    s += str(nombre) + '\n'

print(s)