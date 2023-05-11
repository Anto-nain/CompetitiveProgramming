top1 = 0
top2 = 0
top3 = 0
entry = 0
while True:
    try:
        e = input()
        if e == '':
            if entry > top3:
                if entry > top2:
                    if entry > top1:
                        top3 = top2
                        top2 = top1
                        top1 = entry
                    else:
                        top3 = top2
                        top2 = entry
                else:
                    top3 = entry
            entry = 0
        else:
            entry += int(e)
    except:
        if entry > top3:
                if entry > top2:
                    if entry > top1:
                        top3 = top2
                        top2 = top1
                        top1 = entry
                    else:
                        top3 = top2
                        top2 = entry
                else:
                    top3 = entry
        break
print(top1+top2+top3)