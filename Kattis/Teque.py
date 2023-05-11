n = 0
deque_droit = 2*10**6*[None]
deque_gauche = 2*10**6*[None]
deb_gauche = 10**6
deb_droit = 10**6
fin_gauche = 10**6 - 1
fin_droit = 10**6 - 1
pop_gauche = 0
pop_droit = 0

for i in range(int(input())):
    [action,x] = input().split(' ')
    x = int(x)
    if action == 'push_back':
        if pop_droit + 1 == pop_gauche:
            fin_droit += 1
            deque_droit[fin_droit] = x
            pop_droit += 1
        elif pop_droit == pop_gauche:
            fin_droit += 1
            deque_droit[fin_droit] = x
            fin_gauche += 1
            deque_gauche[fin_gauche] = deque_droit[deb_droit]
            deque_droit[deb_droit] = None
            deb_droit += 1
            pop_gauche += 1
              
    elif action == 'push_front':
        if pop_gauche == pop_droit + 1:
            deb_gauche -= 1
            deque_gauche[deb_gauche] = x
            deque_droit[deb_droit-1] = deque_gauche[fin_gauche]
            deque_gauche[fin_gauche] = None
            fin_gauche -= 1
            deb_droit -= 1
            pop_droit += 1
        elif pop_gauche == pop_droit:
            deb_gauche -= 1
            deque_gauche[deb_gauche] = x
            pop_gauche += 1
    elif action == 'push_middle':
        if pop_gauche == pop_droit:
            fin_gauche += 1
            pop_gauche += 1
            deque_gauche[fin_gauche] = x
        elif pop_gauche == pop_droit + 1:
            deb_droit -= 1
            pop_droit += 1
            deque_droit[deb_droit] = x    
    else:
        if x >= pop_gauche:
            print(deque_droit[deb_droit + x - pop_gauche])  
        else:
            print(deque_gauche[deb_gauche + x])    