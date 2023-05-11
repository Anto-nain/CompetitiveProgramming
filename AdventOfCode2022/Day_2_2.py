score = 0
while True:
    try:
        t = input().split()
        if t[0] == 'A':
            if t[1] == 'X':
                score += 3
            elif t[1] == 'Y':
                score += 4
            else:
                score += 8
        elif t[0] == 'B':
            if t[1] == 'X':
                score += 1
            elif t[1] == 'Y':
                score += 5
            else:
                score += 9
        else :
            if t[1] == 'X':
                score += 2
            elif t[1] == 'Y':
                score += 6
            else:
                score += 7
    except:
        break
print(score)