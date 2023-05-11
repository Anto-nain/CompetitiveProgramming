entry = 0
max = 0
id_max = 0
i = 1
while True:
    try:
        e = input()
        if e == '':
            if entry > max:
                max = entry
                id_max = i
            entry = 0
            i += 1
        else:
            entry += int(e)
    except:
        if entry > max:
                max = entry
                id_max = i
        break
print(id_max,max)
            
    