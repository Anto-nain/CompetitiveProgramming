T = int(input())
for t in range(T):
    tag = 'Case #'+str(t+1)+': '
    N = int(input())
    
    num_alph = int((-1+(1+4*N/13)**0.5)/2)
    n_restant = N-26*(num_alph+1)*num_alph//2
    
    lettre = (n_restant-1)//(num_alph+1) +1
    
    print(tag+chr(ord('A')+lettre-1))
    