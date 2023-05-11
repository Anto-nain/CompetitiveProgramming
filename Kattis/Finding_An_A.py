S=''
mot = input()
go = True
for i in range(len(mot)):
    if mot[i] == 'a':
        go = False
    if not go:
        S += mot[i]
print(S)