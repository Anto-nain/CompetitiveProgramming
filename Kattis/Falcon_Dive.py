M,N,C = input().split(' ')
M = int(M)
N = int(N)
C = C[1]

image1 = []
for i in range(M):
    t = input()
    image1.append([t[e] for e in range(N)])
input()
image2 = []
for i in range(M):
    t = input()
    image2.append([t[e] for e in range(N)])

silhouette = []
faucon1 = []
faucon2 = []
back = [[None for k in range(N)] for e in range(M)]

for i in range(M):
    for j in range(N):
        if image1[i][j] == C:
            faucon1.append([i,j])
            back[i][j] = image2[i][j]
        elif image2[i][j] == C:
            faucon2.append([i,j])
            back[i][j] = image1[i][j]
        else:
            back[i][j] = image2[i][j]

deplacement = [faucon2[0][0]-faucon1[0][0],faucon2[0][1]-faucon1[0][1]]


for a in faucon2:
    i = a[0]+deplacement[0]
    j = a[1]+deplacement[1]
    if 0 <= i < M and 0 <= j < N:
        back[i][j] = C



for k in range(M):
    l = ''
    for u in range(N):
        l = l + back[k][u]
    print(l)