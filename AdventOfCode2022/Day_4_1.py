nb = 0
while True:
    try:
        e,f = input().split(',')
    except :
        break
    e = list(map(int,e.split('-')))
    f = list(map(int,f.split('-')))
    if e[0] <= f[0] and e[1] >= f[1]:
        nb += 1
    elif e[0] >= f[0] and e[1] <= f[1]:
        nb += 1
print(nb)
    
    
    