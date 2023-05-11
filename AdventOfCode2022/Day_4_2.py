nb = 0
while True:
    try:
        e,f = input().split(',')
    except :
        break
    e = list(map(int,e.split('-')))
    f = list(map(int,f.split('-')))
    if f[1] >= e[1] >= f[0] or f[1] >= e[0] >= f[0] or e[1] >= f[0] >= e[0] or e[1] >= f[1] >= e[0]:
        #print(e,f)
        nb += 1
print(nb)
    
    
    