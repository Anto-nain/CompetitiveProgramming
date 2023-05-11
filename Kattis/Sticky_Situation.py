N = int(input())
L = sorted(list(map(int, input().split())))

impossible = True
i = 0
while impossible and i < N - 2:
    if L[i] + L[i+1] > L[i + 2]:
        impossible = False
    i += 1

if impossible:
    print('impossible')
else:
    print('possible')