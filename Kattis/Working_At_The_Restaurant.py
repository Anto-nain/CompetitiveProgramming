while True:
    N = int(input())
    if N == 0:
        break

    L = []
        
    for i in range(N):
        L.append(input().split(' '))
        L[-1][1] = int(L[-1][1])
    
    id_drop = 1
    id_take = 2
    assiette_drop = 0
    assiette_take = 0
    i = 0

    while True:
        if L[i][0] == 'DROP':
            assiette_drop += L[i][1]
            print('DROP ' + str(id_drop) + ' ' + str(L[i][1]))
            i += 1
    
        else:
            nb_take = 0
            while True:
                try:
                    if L[i + nb_take][0] == 'TAKE':
                       nb_take +=  1
                    else:
                        break
                except:
                    break

            for j in range(nb_take):
                if assiette_take == 0:
                    print('MOVE ' + str(id_drop) + '->' + str(id_take) + ' ' + str(assiette_drop))
                    assiette_take = assiette_drop
                    assiette_drop = 0
                    print('TAKE ' + str(id_take) + ' ' + str(L[i+j][1]))
                    assiette_take -= L[i+j][1]
                elif assiette_take < L[i+j][1]:
                    combien = L[i+j][1]
                    print('TAKE ' + str(id_take) + ' ' + str(assiette_take))
                    combien -= assiette_take
                    print('MOVE ' + str(id_drop) + '->' + str(id_take) + ' ' + str(assiette_drop))
                    assiette_take = assiette_drop - combien
                    assiette_drop = 0
                    print('TAKE ' + str(id_take) + ' ' + str(combien))
                else:
                    print('TAKE ' + str(id_take) + ' ' + str(L[i+j][1]))
                    assiette_take -= L[i+j][1]
            i += nb_take
        if i >= len(L):
            break
    print('')
