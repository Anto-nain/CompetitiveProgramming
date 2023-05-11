sum = 0

while True:
    try:
        t1 = input()
        t2 = input()
        t3 = input()
    except:
        break
    for e in t1:
        if e in t2 and e in t3:
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