N = int(input())
M = int(input())
entries = list(map(int,input().split()))
exits = list(map(int,input().split()))
d = {}

for i in range(N):
    for j in range(M):
        if entries[i]<exits[j]:
            dt = exits[j]-entries[i]
            if dt not in d:
                d[dt] = 0
            d[dt] += 1
max = -1
id = None
for e in d:
    if d[e] > max:
        max = d[e]
        id = e
print(id)