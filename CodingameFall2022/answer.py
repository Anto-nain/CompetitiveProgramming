import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def chn(i,j):
    return str(i)+' '+str(j)
def indice(ch):
    return list(map(int,ch.split()))


width, height = [int(i) for i in input().split()]
mid  = [width//2,height//2]
map_cases = set()
for i in range(width):
    for j in range(height):
        map_cases.add(chn(i,j))

my_matter = 10



# game loop
tour=0
side = None
divided = False


while True:
    my_matter, opp_matter = [int(i) for i in input().split()]
    recycleurs_adverses = set()
    recycleurs_moi = set()
    robots_adverses = {}
    robots_moi = {}
    cases_adverses = set()
    cases_moi = set()
     
    map_scrap_amount = {}
    map_owner = {}
    map_units = {}
    map_recycler = {}
    map_can_build = {}
    map_can_spawn = {}
    map_in_range_of_recycler = {}
    map_expand = set()
    
    sortie = ''
    
    for j in range(height):
        for i in range(width):
            # owner: 1 = me, 0 = foe, -1 = neutral
            scrap_amount, owner, units, recycler, can_build, can_spawn, in_range_of_recycler = [int(k) for k in input().split()]
            if recycler == 1:
                if owner == 0:
                    recycleurs_adverses.add(chn(i, j))
                else:
                    recycleurs_moi.add(chn(i, j))
            if units > 0:
                if owner == 0:
                    robots_adverses[chn(i, j)] = units
                else:
                    robots_moi[chn(i, j)] = units
            if owner == 0:
                cases_adverses.add(chn(i, j))
            elif owner == 1:
                cases_moi.add(chn(i, j))
            if owner != 0 and scrap_amount != 0:
                map_expand.add(chn(i,j))
                
            
            map_scrap_amount[chn(i,j)] = scrap_amount
            map_owner[chn(i,j)] = owner
            map_units[chn(i,j)] = units
            map_recycler[chn(i,j)] = recycler
            map_can_build[chn(i,j)] = can_build
            map_can_spawn[chn(i,j)] = can_spawn
            map_in_range_of_recycler[chn(i,j)] = in_range_of_recycler
            
            
            
    # Initialisation des déplacements        

    mineur = set()
    danger = set()
    neutre = set()
    
    if tour==0:
        for case in cases_moi:
            if map_units[case] == 0:
                start = indice(case)
        side=[]
        deplacement = []
        if start[0]<mid[0]:
            side.append('left')
            deplacement.append([1,0])
            if start[1]<mid[1]:
                side.append('top')
                deplacement.append([0,1])
                deplacement.append([0,-1])
                deplacement.append([-1,0])
            else:
                side.append('bot')
                deplacement.append([0,-1])
                deplacement.append([0,1])
                deplacement.append([-1,0])
        else:
            side.append('right')
            deplacement.append([-1,0])
            if start[1]<mid[1]:
                side.append('top')
                deplacement.append([0,1])
                deplacement.append([0,-1])
                deplacement.append([1,0])
            else:
                side.append('bot')
                deplacement.append([0,-1])
                deplacement.append([0,1])
                deplacement.append([1,0])
                
        sortie += 'BUILD '+chn(start[0],start[1])+';'
        for case in cases_moi:
            neutre.add(case)
        
    #V1 début
  
    
    # Séparation des robots en fonction de leurs ennemis à proximité
    
    else:        
        for cha in robots_moi:       
            i,j = indice(cha)
            job = 'neutre'
            for che in robots_adverses:
                k,l = indice(che)
                if abs(i-k)+abs(j-l) <= 2:
                    job = 'danger'
                elif job != 'danger':
                    job = 'neutre'
            if job == 'danger':
                danger.add(cha)
            elif job == 'neutre':
                neutre.add(cha)




                
        # Actions défensives / offensives
        # On sélection l'ennemi proche ayant la plus grande force, si possible on SPAWN jusqu'à avoir sa taille, si notre taille était plus grande, on s'avance vers lui  
    
    for robot in danger:
        x,y = indice(robot)
        unit = map_units[robot]
        taille_max = 0
        position = None
        for alentour in [[0,1],[0,-1],[1,0],[-1,0],[0,-2],[-1,-1],[-2,0],[-1,1],[0,2],[1,-1],[2,0],[1,1]]:
            if chn(x+alentour[0],y+alentour[1]) in map_cases and map_units[chn(x+alentour[0],y+alentour[1])] > 0 and map_owner[chn(x+alentour[0],y+alentour[1])] == 0:
                nb = map_units[chn(x+alentour[0],y+alentour[1])]
                if nb > taille_max:
                    taille_max = nb
                    position = chn(x+alentour[0],y+alentour[1])
        if position != None:
            nb = min(my_matter//10,taille_max+1-unit)
            if nb>0:
                sortie+='SPAWN '+str(nb)+' '+robot+';'
                my_matter -= 10*nb
            else:
                sortie += 'MOVE '+str(taille_max+1)+' '+robot+' '+position+';'
                
                
    # Construction des recycleurs
    n = len(recycleurs_moi)
    if n < 4:
        for case in cases_moi:
            x,y = indice(case)
            build = True
            for rec in recycleurs_moi:
                rx,ry = indice(rec)
                if abs(x-rx)+abs(y-ry) <3:
                    build = False
            if build and n !=4 :
                sortie += 'BUILD '+case+';'
                n+=1
                recycleurs_moi.add(case)
                    
                    
        
    
    
    '''
    
    pref1 = None
    max1 = 0
    pref2 = None
    max2 = 0
    for case_chn in cases_moi:
        if map_owner[case_chn] == 1 and map_can_build[case_chn] == 1:
            case = indice(case_chn)
            scrap = 0
            for dep in deplacement:
                if chn(case[0]+dep[0],case[1]+dep[1]) in map_cases and map_in_range_of_recycler[chn(case[0]+dep[0],case[1]+dep[1])]:
                    scrap += map_scrap_amount[chn(case[0]+dep[0],case[1]+dep[1])]
            if scrap > max1 :
                    pref2 = pref1
                    max2 = max1
                    max1 = scrap
                    pref1 = case_chn
            elif scrap > max2:
                pref2 = case_chn
                max2 = scrap

    if pref1 != None and my_matter >= 10:
        sortie += 'BUILD '+pref1+';'
        my_matter -= 10
        if pref2 != None and my_matter >= 10 and 0==1:
            sortie += 'BUILD '+pref2+';'
            my_matter -= 10
    else:
        sortie += 'MESSAGE MEEEEERDE;'
    '''
            
    # Actions neutres
    #On déplace nos robots vers les cases d'où on peut expand
    
    for robot in neutre:
        x,y = indice(robot)
        unit = map_units[robot]
        a_enlever = set()
        for _ in range(unit):
            meilleur_deplacement = None
            nb_next_expand = 0
            for dep in deplacement:
                if chn(x+dep[0],y+dep[1]) in map_cases and chn(x+dep[0],y+dep[1]) in map_expand and chn(x+dep[0],y+dep[1]) not in a_enlever:
                    nb = 0
                    for nex in deplacement:
                        if chn(x+dep[0]+nex[0],y+dep[1]+nex[1]) in map_cases and chn(x+dep[0]+nex[0],y+dep[1]+nex[1]) in map_expand and chn(x+dep[0],y+dep[1]) not in a_enlever:
                            nb += 1
                    if nb > nb_next_expand:
                        meilleur_deplacement = chn(x+dep[0],y+dep[1])
                        nb_next_expand = nb
               
            
            if meilleur_deplacement != None:
                a_enlever.add(meilleur_deplacement)
                sortie += 'MOVE 1 '+robot+' '+meilleur_deplacement+';'
            
        for e in a_enlever:
            map_expand.remove(e)
    
    
    # On fait spawn des robots proche de cases où on peut expand
    
    for case in map_can_spawn:
        a_enlever = set()
        if map_can_spawn[case] == 1 and map_owner[case] == 1:
            nb = 0
            for dep in deplacement:
                if chn(x+dep[0],y+dep[1]) in map_cases and chn(x+dep[0],y+dep[1]) in map_expand and chn(x+dep[0],y+dep[1]) not in a_enlever:
                    nb += 1
                    a_enlever.add(chn(x+dep[0],y+dep[1]))
            sortie += 'SPAWN '+str(nb) + ' ' + case+';'
            for e in a_enlever:
                map_expand.remove(e)
    # V1 fin 
        
    '''
    # V2 début
    
    if not divided:
        for robot in robots_moi:
            x,y = indice(robot)
            unit = map_units[robot]
            if indice(robot)[0] != mid[0]+1:
                a_enlever = set()
                for _ in range(unit):
                    meilleur_deplacement = None
                    nb_next_expand = 0
                    for dep in deplacement:
                        if chn(x+dep[0],y+dep[1]) in map_cases and chn(x+dep[0],y+dep[1]) in map_expand and chn(x+dep[0],y+dep[1]) not in a_enlever:
                            nb = 0
                            for nex in deplacement:
                                if chn(x+dep[0]+nex[0],y+dep[1]+nex[1]) in map_cases and chn(x+dep[0]+nex[0],y+dep[1]+nex[1]) in map_expand and chn(x+dep[0],y+dep[1]) not in a_enlever:
                                    nb += 1
                            if nb > nb_next_expand:
                                meilleur_deplacement = chn(x+dep[0],y+dep[1])
                                nb_next_expand = nb
                    
                    
                    if meilleur_deplacement != None:
                        a_enlever.add(meilleur_deplacement)
                        sortie += 'MOVE 1 '+robot+' '+meilleur_deplacement+';'
                    
                for e in a_enlever:
                    map_expand.remove(e)
                    
            else:
                if chn() in
                
    '''
        
        
                    
    '''           
                    

    # Actions

    for robot in robots_moi:        
        for dep in deplacement:
            if chn(robot[0]+dep[0],robot[1]+dep[1]) in map_can_build and map_can_build[chn(robot[0]+dep[0],robot[1]+dep[1])] == 1 and map_in_range_of_recycler[chn(robot[0]+dep[0],robot[1]+dep[1])] == 0:
                if my_matter >= 20:
                    sortie += 'BUILD '+chn(robot[0]+dep[0],robot[1]+dep[1])+';'                
    
        for dep in deplacement:
            if chn(robot[0]+dep[0],robot[1]+dep[1]) in map_owner:
                if map_owner[chn(robot[0]+dep[0],robot[1]+dep[1])] == 0 :
                    sortie += 'MOVE '+str(map_units[chn(robot[0],robot[1])])+' '+chn(robot[0],robot[1])+' '+chn(robot[0]+dep[0],robot[1]+dep[1])+';'
                elif map_owner[chn(robot[0]+dep[0],robot[1]+dep[1])] == -1 :
                    sortie += 'MOVE '+str(map_units[chn(robot[0],robot[1])])+' '+chn(robot[0],robot[1])+' '+chn(robot[0]+dep[0],robot[1]+dep[1])+';'
        
        taille_max = 0
        position = None
        
        for alentour in [[0,1],[0,-1],[1,0],[-1,0],[0,-2],[-1,-1],[-2,0],[-1,1],[0,2],[1,-1],[2,0],[1,1]]:
            if chn(robot[0]+alentour[0],robot[1]+alentour[1]) in map_units and map_units[chn(robot[0]+alentour[0],robot[1]+alentour[1])] > 0 and map_owner[chn(robot[0]+alentour[0],robot[1]+alentour[1])] == 0:
                nb = map_units[chn(robot[0]+alentour[0],robot[1]+alentour[1])]
                if nb > taille_max:
                    taille_max = nb
                    position = chn(robot[0]+alentour[0],robot[1]+alentour[1])
                    
        if position != None:
            nb = min(my_matter//10,taille_max+1-map_units[chn(robot[0],robot[1])])
            if nb>0:
                sortie+='SPAWN '+str(nb)+' '+chn(robot[0],robot[1])+';'
            
    ''' 
    
    if sortie != '':
        sortie = sortie[:-1]
    else:
        sortie = 'WAIT'
    print(sortie)
    
    
    my_matter += 10
    tour+=1




    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


