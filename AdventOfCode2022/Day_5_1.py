tab = [['Z','J','N','W','P','S'],['G','S','T'],['V','Q','R','L','H'],['V','S','T','D'],['Q','Z','T','D','B','M','J'],['M','W','T','J','D','C','Z','L'],['L','P','M','W','G','T','J'],['N','G','M','T','B','F','Q','H'],['R','D','G','C','P','B','Q','W']]
#tab = [['Z','N'],['M','C','D'],['P']]

def move(tab,fr0m,to):
    if fr0m == to:
        return tab
    else:
        tab[to].append(tab[fr0m].pop())
        return tab

while True:
    try:
        t = input().split()
    except:
        break
    
    nb = int(t[1])
    fr0m = int(t[3])-1
    to = int(t[5])-1
    for i in range(nb):
        tab = move(tab,fr0m,to)
        #print(tab)
s=''
for i in range(len(tab)):
    s += tab[i][-1]
print(s)
    
    