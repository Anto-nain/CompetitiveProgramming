objectif = list(map(int,input().split(' ')))
n = int(input())
L = []
for o in range(n):
   L.append(input())

def multiply(ligne, m):
    return ([ligne[0]*m[0][0]+ligne[1]*m[1][0],ligne[0]*m[0][1]+ligne[1]*m[1][1]])
            

def trajet(instructions):
    direction = [0,1]
    matrice = [[0,1],[-1,0]]
    coords = [0,0]

    for instr in instructions:
        if instr == 'Forward':
            coords[0] += direction[0]
            coords[1] += direction[1]
        elif instr == 'Left':
            direction = multiply(direction,matrice)
        else:
            direction = multiply(multiply(multiply(direction,matrice),matrice),matrice)
    return coords
        



   
for l in range(n):
    choix = {'Forward','Right','Left'}
    choix.remove(L[l])
    stop = False
    for direction in choix:
        instructions = [c for c in L]
        instructions[l] = direction 
        if trajet(instructions) == objectif:
            stop = True
            break
    if stop:
        break

print(str(l+1) + ' ' + direction)