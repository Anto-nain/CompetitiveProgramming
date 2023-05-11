P = int(input())
L = []
for i in range(P):
    t = list(map(int,input().split(' ')))
    print(str(t[0])+' '+str(int(t[1]*(t[1]+1)/2+t[1])))
    