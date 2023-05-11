N = int(input())

L = []

for i in range(N):
    L.append(input())
    

L_tri = sorted(L)

if L == L_tri:
    print('INCREASING')
elif L == L_tri[::-1]:
    print('DECREASING')
else:
    print('NEITHER')