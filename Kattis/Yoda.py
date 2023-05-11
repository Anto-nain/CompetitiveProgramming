N = input()
M = input()
A = max(len(N),len(M))

N_bis = M_bis = ''

if len(N) > len(M):
    k = len(N) - len(M)
    M = k*'0' + M
elif len(N) < len(M):
    k = len(M) - len(N)
    N = k*'0' + N 

for i in range(A):
    if int(N[-1]) > int(M[-1]):
        N_bis = N[-1] + N_bis
    elif int(N[-1]) < int(M[-1]):
        M_bis = M[-1] + M_bis
    else:
        M_bis = M[-1] + M_bis
        N_bis = N[-1] + N_bis
    M = M[:-1]
    N = N[:-1]
            
if N_bis == '':
    print('YODA')
else: 
    print(int(N_bis))
if M_bis == '':
    print('YODA')
else:
    print(int(M_bis))
    