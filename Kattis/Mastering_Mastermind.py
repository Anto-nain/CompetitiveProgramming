[n,code,guess] = input().split(' ')
n = int(n)
r,s = 0,0

reste_code = {}
reste_guess = {}

for i in range(n):
    if code[i] == guess[i]:
        r += 1
    else:
        try:
            reste_code[code[i]] += 1
        except:
            reste_code[code[i]] = 1
        try:
            reste_guess[guess[i]] += 1
        except:
            reste_guess[guess[i]] = 1

for e in reste_code:
    if e in reste_guess:
        s += min(reste_code[e],reste_guess[e])
        
print(str(r) + ' ' + str(s))
