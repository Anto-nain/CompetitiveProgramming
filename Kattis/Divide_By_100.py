N = input()
M = input()

n = len(M[1:])
if n >= len(N):
    mot = '0.' + '0'*(n-len(N)) + N
else:
    i=len(N)-n
    mot = N[:i] + '.' + N[i:]

while mot[-1] == '0':
    mot = mot[:-1]
if mot[-1] == '.':
    mot = mot[:-1]
print(mot)