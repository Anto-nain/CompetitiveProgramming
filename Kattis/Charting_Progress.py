
n=1
L = []
while True:
    try:
        ligne = input()
        L.append(ligne)
        if ligne == '':
            n += 1
    except:
        break


l=0
fin = len(L)

def tri(L,l,occupé):
    max = len(L[l])
    nb = 0
    for i in range(max):
        if L[l][i] == "*":
            nb += 1
    print((max-nb-occupé)*'.'+nb*'*'+occupé*'.')
    return nb


for i in range(n):
    occupé = 0
    while l != fin and L[l] != '':
        occupé += tri(L,l,occupé)
        l+=1
    if l == fin:
        break
    l+=1
    print('\n')

