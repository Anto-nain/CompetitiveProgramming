[t,s,n] = list(map(int,input().split(' ')))
L = list(map(int,input().split(' ')))
L = L + [t]
down = s
for i in range(1,len(L)):
    down = L[i] - L[i-1] + (s-down)
    if down > s:
        down = s


print(s-down)