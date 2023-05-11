sum = 0

while True:
    try:
        t = input()
    except:
        break
    l = len(t)
    left = t[0:l//2]
    #print(left)
    right = t[l//2:l]
    #print(right)
    for e in left:
        if e in right:
            break
    
    if e.lower() == e:
        #print(e)
        #print(ord(e)-ord('a')+1)
        sum += ord(e)-ord('a')+1
    else:
        #print(e)
        #print(ord(e)-ord('A')+27)
        sum += ord(e)-ord('A')+27
         
    
print(sum)