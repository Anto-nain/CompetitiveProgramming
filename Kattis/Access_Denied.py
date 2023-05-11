L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']


n=1
entree = 'a'
print(entree)
t = input()
while t == "ACCESS DENIED (5 ms)":
    n += 1
    entree = n*'a'
    print(entree)
    t = input()
    temps = int(t.split('(')[1][0])

def test_mdp(mdp):
    print(mdp)
    t = reponse(mdp)
    if t == 'ACCESS GRANTED':
        return t,None
    else:
        a = t.split('(')
        return t,int(a[1][0])

def reponse(mdp):
    vrai = 'Ant0n1'
    if len(mdp) != len(vrai):
        return 'ACCESS DENIED (5 ms)'
    elif:
        t = 5
        for i in range(len(vrai)):
            t += 4
            if vrai[i] != mdp[i]:
                t += 1
                return 'ACCESS DENIED (' + str(t) + ' ms)'
    return 'ACCESS GRANTED'

if t != 'ACCESS GRANTED':
    n_lettre = 0
    test_lettre = 1
    max_lettre = len(L)
    mdp = n*'a'
    sauvegarde_mdp = mdp
    while t != 'ACCESS GRANTED':
        mdp[n_lettre] = L[test_lettre]
        t,nouveau_temps = test_mdp(mdp)
        if nouveau_temps < temps:
            mdp = sauvegarde_mdp
            n_lettre += 1
            test_lettre = 1
        elif nouveau_temps > temps:
            n_lettre += 1
            test_lettre = 1
            temps = nouveau_temps
        else:
            test_lettre += 1
        
            
            
        
        
        
            

    
    