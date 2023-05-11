S = input()
T,C,G = 0,0,0
for l in S:
    if l == 'T':
        T += 1
    elif l == 'C':
        C += 1
    else:
        G += 1
print(T**2 + G**2 + C**2 + 7*min(T,C,G))