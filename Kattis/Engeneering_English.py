
dico = {}

while True:
    try:
        l = input().split(' ')



        R = ''
        for mot in l:
            if mot.lower() not in dico:
                dico[mot.lower()] = None
                R += mot + ' '
            else:
                R += '. '

        R = R[:-1]
        print(R)
    except:
        break