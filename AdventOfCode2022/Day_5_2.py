tab = [['Z','J','N','W','P','S'],['G','S','T'],['V','Q','R','L','H'],['V','S','T','D'],['Q','Z','T','D','B','M','J'],['M','W','T','J','D','C','Z','L'],['L','P','M','W','G','T','J'],['N','G','M','T','B','F','Q','H'],['R','D','G','C','P','B','Q','W']]
#tab = [['Z','N'],['M','C','D'],['P']]

def move(tab,nb,fr0m,to):
    if fr0m == to:
        return tab
    else:
        t = tab[fr0m][len(tab[fr0m])-nb:len(tab[fr0m])]
        for i in range(nb):
            tab[fr0m].pop()
        tab[to] = tab[to] + t
        return tab

while True:
    try:
        t = input().split()
    except:
        break
    
    nb = int(t[1])
    fr0m = int(t[3])-1
    to = int(t[5])-1
    #print(tab,nb,fr0m,to)
    move(tab,nb,fr0m,to)

s=''
for i in range(len(tab)):
    s += tab[i][-1]
print(s)
    
    