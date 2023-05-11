
mat = []
for i in range(4):
    mat.append(list(map(int,input().split(' '))))

dir = int(input())

def rota(M): #vers la droite
    return([[M[3][0],M[2][0],M[1][0],M[0][0]],
           [M[3][1],M[2][1],M[1][1],M[0][1]],
           [M[3][2],M[2][2],M[1][2],M[0][2]],
           [M[3][3],M[2][3],M[1][3],M[0][3]]])

def ecriture(M):
    i = 0
    print(str(M[i][0]) + ' ' + str(M[i][1]) + ' ' + str(M[i][2]) + ' ' + str(M[i][3]))
    i = 1
    print(str(M[i][0]) + ' ' + str(M[i][1]) + ' ' + str(M[i][2]) + ' ' + str(M[i][3]))
    i = 2
    print(str(M[i][0]) + ' ' + str(M[i][1]) + ' ' + str(M[i][2]) + ' ' + str(M[i][3]))
    i = 3
    print(str(M[i][0]) + ' ' + str(M[i][1]) + ' ' + str(M[i][2]) + ' ' + str(M[i][3]))


def input_gauche(M):
    it = 0
    blocage = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
    go = True
    memoire = [[elem for elem in ligne] for ligne in M]
    while go:
        for j in range(1,4):
            for i in range(4):
                if M[i][j] == 0:
                    pass
                elif M[i][j-1] == 0:
                    M[i][j-1] = M[i][j]
                    M[i][j] = 0
                    blocage[i][j-1] = blocage[i][j]
                    blocage[i][j] = False
                elif M[i][j-1] == M[i][j] and not blocage[i][j-1] and not blocage[i][j]:
                    M[i][j-1] *= 2
                    M[i][j] = 0
                    blocage[i][j-1] = True
        if memoire == M:
            go = False
        else:
            memoire = [[elem for elem in ligne] for ligne in M]
        it += 1
    return M

if dir == 1:
    mat = rota(rota(rota(mat)))
elif dir == 2:
    mat = rota(rota(mat))
elif dir == 3:
    mat = rota(mat)

mat = input_gauche(mat)

if dir == 3:
    mat = rota(rota(rota(mat)))
elif dir == 2:
    mat = rota(rota(mat))
elif dir == 1:
    mat = rota(mat)



ecriture(mat)
                    