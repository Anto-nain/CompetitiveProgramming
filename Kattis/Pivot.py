n = int(input())
L = list(map(int,input().split(' ')))

check = [0]*n

max_gauche = - 2**32
min_droite = 2**32


for i in range(0,n):
    if max_gauche < L[i]:
        max_gauche = L[i]
        check[i] += 0.5
    if L[n-1-i] < min_droite:
        check[n-1-i] += 0.5
        min_droite = L[n-1-i]

res = sum(list(map(int,check)))

    
print(res)