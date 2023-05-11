X = int(input())
N = int(input())
L = []
for i in range(N):
    L.append(int(input()))

print((N+1)*X-sum(L))