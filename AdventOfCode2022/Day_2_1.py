score = 0
while True:
    try:
        t = input().split()
        if t[1] == 'X':
            score += 1
            if t[0] == 'A':
                score += 3
            elif t[0] == 'B':
                pass
            else:
                score += 6
        elif t[1] == 'Y':
            score += 2
            if t[0] == 'A':
                score += 6
            elif t[0] == 'B':
                score += 3
            else:
                pass
        else:
            score += 3
            if t[0] == 'A':
                pass
            elif t[0] == 'B':
                score += 6
            else:
                score += 3
    except:
        break
    
print(score)
        
    