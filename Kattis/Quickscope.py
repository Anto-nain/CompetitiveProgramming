import sys

inp = sys.stdin.read().split('\n')


niveau = 0
var = dict()
global_stop = False

for i in range(1,int(inp[0])+1):
    
    enter = inp[i].split(' ')
    
    if global_stop:
        break
    if enter[0] == '{':
        niveau += 1
    elif enter[0] == '}':
        niveau -= 1
        for v in var:
            if niveau+1 in var[v]:
                del var[v][niveau+1]
    elif enter[0] == 'TYPEOF':
        v = enter[1]
        if v in var:
            if niveau in var[v]:
                sys.stdout.write(var[v][niveau] + '\n')
            else:
                n = niveau - 1
                trouve = False
                while n >= 0 :
                    if n in var[v]:
                        sys.stdout.write(var[v][n] + '\n')
                        trouve = True
                        break
                    else:
                        n -= 1
                if not trouve:
                    sys.stdout.write('UNDECLARED' + '\n')                 
        else:
            sys.stdout.write('UNDECLARED' + '\n')
    else:
        v = enter[1]
        val = enter[2]
        if v not in var:
            var[v] = {}       
        if niveau not in var[v]:
            var[v][niveau] = val
        else :
            sys.stdout.write('MULTIPLE DECLARATION' + '\n')
            global_stop = True
        
'''
        print('TYPEOF')
        print('variable',v)
        print('valeur',val)
        print('niveau',niveau)
        print(var)
'''
        
