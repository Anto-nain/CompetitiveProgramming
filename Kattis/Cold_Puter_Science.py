n = int(input())
T = map(int,input().split(' '))
S = 0
for a in T:
    if a < 0:
        S += 1
print(S)