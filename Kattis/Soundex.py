K = []
while True:
    try:
        K.append(input())
    except:
        break

# transformation soundex
R = []
for mot in K:
    M = ''
    for i in range(len(mot)):
        lettre = mot[i]
        if lettre in ['B','F','P','V']:
            M = M + '1'
        elif lettre in ['C','G','J','K','Q','S','X','Z']:
            M = M + '2'
        elif lettre in ['D','T']:
            M = M + '3'
        elif lettre == 'L':
            M = M + '4'
        elif lettre in ['M','N']:
            M = M + '5'
        elif lettre == 'R':
            M = M + '6'
        else :
            M = M + 'Z'
        
    R.append(M)

for i in range(len(R)):
    mot = R[i]
    sauvegarde = None
    M = ''
    for j in range(len(mot)):
        lettre = mot[j]
        if lettre == 'Z':
            sauvegarde = None
        elif lettre != sauvegarde:
            sauvegarde = lettre
            M = M + lettre       
    R[i] = M
    

for mot in R:
    print(mot)