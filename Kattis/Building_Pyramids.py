N = int(input())
max = 0
while N > 0:
    N-=(2*max+1)**2
    max+=1
if N == 0:
    print(max)
else:
    print(max-1)