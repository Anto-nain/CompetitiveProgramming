[G,T,N] = map(int,input().split(' '))
W = map(int,input().split(' '))
print(int(0.9*(G-T)-sum(W)))