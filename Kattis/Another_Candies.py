t = input()
T = int(t)
t = input()

liste_cas=[]
for i in range(T):
    bonbons = 0
    enfants = 0
    go = True
    while go:
        try:
            t = input()
        except:
            go = False
        if t == '':
            go = False
        else :
            bonbons+=int(t)
            enfants += 1
    liste_cas.append([bonbons,enfants])
            
        
for i in range(T):
    if liste_cas[i][0]%liste_cas[i][1] == 0:
        print('YES')
    else:
        print('NO')
