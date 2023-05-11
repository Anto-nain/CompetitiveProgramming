
for i in range(int(input())):
    L = []
    for j in range(int(input())):
        L.append(list(map(int,input().split(' '))))
        L[-1] = -L[-1][0]*(-L[-1][1]/(2*(-L[-1][0])))**2 + L[-1][1]*(-L[-1][1]/(2*(-L[-1][0]))) + L[-1][2]
    m = 0
    max = L[0]
    for l in range(len(L)):
        if max < L[l]:
            max = L[l]
            m = l
    print(m+1)
        
