N = int(input())
D = {}
for i in range(N):
    t = input().split(' ')
    D[t[0]] = t[1]

m_hg,m_hd,m_bg,m_bd = 0,0,0,0
b_hg,b_hd,b_bg,b_bd = 0,0,0,0

for e in D:
    if D[e] == 'm':
        if e[0] == '+':
            m_hg += 1
        elif e[0] == '-':
            m_bg += 1
        elif e[1] ==  '+':
            m_hd += 1
        else:
            m_bd += 1
    else:
        if e[0] == '+':
            b_hg += 1
        elif e[0] == '-':
            b_bg += 1
        elif e[1] ==  '+':
            b_hd += 1
        else:
            b_bd += 1

droite = True
gauche = True

if b_hg != 0 or b_bg != 0:
    gauche = False
if b_hd != 0 or b_bd != 0:
    droite = False
if m_hg == 8 or m_bg == 8:
    gauche = False
if m_hd == 8 or m_bd == 8:
    droite = False

#print(m_hg,m_hd,m_bg,m_bd)
#print(b_hg,b_hd,b_bg,b_bd)
#print(droite,gauche)


if droite:
    print(1)
elif gauche:
    print(0)
else:
    print(2)

