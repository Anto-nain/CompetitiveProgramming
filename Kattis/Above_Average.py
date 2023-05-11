C = int(input())


for i in range(C):
    data=list(map(int,input().split(' ')))
    data.pop(0)
    m = sum(data)/len(data)
    nb = 0
    for note in data:
        if note > m:
            nb += 1
    p = nb*100/len(data)
    p = str(round(p,3))
    l = p.split('.')
    if len(l[1]) > 3:
        print(l[0]+'.'+l[1][:3]+'%')  
    else:
        print(l[0]+'.'+l[1]+(3-len(l[1]))*'0'+'%')
        
