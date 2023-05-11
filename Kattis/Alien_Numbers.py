from math import log, exp

T = int(input())
for t in range(T):
    l = ['Case #'+str(t+1)+': ']
    alien_number,source_language,target_language = input().split()
    source = {}
    n_number = len(alien_number)
    n_source = len(source_language)
    n_target = len(target_language)
    nombre = 0
    #print(alien_number,source_language,target_language,n_source)
    for i in range(n_source):
        source[source_language[i]] = i #source = {caractere : nb en base 10}
    #print(source)
    for k in range(n_number):
        nombre +=source[alien_number[n_number-k-1]]*(n_source**k)
    target={}
    for j in range(n_target):
        target[j]=target_language[j]
        
    nombre = n_target*nombre+1
    nb_ajout = int(log(nombre)/log(n_target))
    for i in range(nb_ajout):
        l.append(target[(nombre//(n_target**(nb_ajout-i)))])
        nombre %= (n_target**(nb_ajout-i))
    print(''.join(l))