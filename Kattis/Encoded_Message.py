for i in range(int(input())):
    mot = input()
    d = int(len(mot)**0.5)
    mot_tr = ''
    for i in range(d**2):
        mot_tr = mot_tr + mot[(d-1-i//d) + d*(((i)%d))]
    print(mot_tr)