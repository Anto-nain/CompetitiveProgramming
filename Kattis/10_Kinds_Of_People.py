r,c = map(int,input().split())

parent = [[[x,y] for y in range(c)] for x in range(r)]
rang = [[1 for i in range(c)] for j in range(r)]
race = [list(input()) for i in range(r)]
#print(parent)
#print(rang)
#print(race)



def find(r,c):
    #print(parent[r][c])
    while not(parent[r][c][0] == r and parent[r][c][1] == c):
        r,c = parent[r][c][0],parent[r][c][1]
    return r,c

def union(r1,c1,r2,c2):
    #print(r1,c1,r2,c2)
    r1,c1 = find(r1,c1)
    r2,c2 = find(r2,c2)
    if (r1 == r2 and c1 == c2) or race[r1][c1] != race[r2][c2]:
        return
    if rang[r1][c1] > rang[r2][c2]:
        parent[r2][c2][0] = r1
        parent[r2][c2][1] = c1
        rang[r1][c1] = rang[r1][c1]+rang[r2][c2]
    else:
        parent[r1][c1][0] = r2
        parent[r1][c1][1] = c2
        rang[r2][c2] = rang[r2][c2]+rang[r1][c1]


for i in range(r):
    for j in range(c):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            union(i,j,i,j-1)
        elif j == 0:
            union(i,j,i-1,j)
        else:
            union(i,j,i-1,j)
            union(i,j,i,j-1)

          

#print(D,tab)
n = int(input())

for i in range(n):
    r1,c1,r2,c2 = map(int,input().split())
    r1,c1 = find(r1-1,c1-1)
    r2,c2 = find(r2-1,c2-1)
    
    if race[r1][c1] != race[r2][c2]:
        print("neither")
    elif race[r1][c1] == '1':
        if r1 == r2 and c1 == c2:
            print("decimal")
        else:
            print("neither")
    else:
        if r1 == r2 and c1 == c2:
            print("binary")
        else:
            print("neither")