common_word = input()
C = len(common_word)
E = int(input())
close_sounding = []

for i in range(E):
    close_sounding.append(input().split(' '))

P = int(input())

phrase_endings = []
for i in range(P):
    phrase_endings.append(input().split(' ')[-1])
liste = []
stop = False
for i in range(E):
    liste_sons = close_sounding[i]
    for son in liste_sons:
        l = len(son)
        if C >= l:
            #print(son,common_word[C-l:C])
            if son == common_word[C-l:C]:
                liste.append(i) 

sons = []
for i in liste:
    sons += close_sounding[i]

for mot in phrase_endings:
    m = len(mot)
    sortie = 'NO'
    for son in sons:
        l = len(son)
        if m >= l:
            if son == mot[m-l:m]:
                sortie = 'YES'
                #print(mot,mot[m-l:m],son)
    print(sortie)
            
            