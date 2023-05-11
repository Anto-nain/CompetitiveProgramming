# from collections import deque
import sys

def main():
    res = ''
    a = list(sys.stdin.read())
    i=0

    while i<len(a) - 1:
        k=a[i]
        if len(a) - 1 -i>2:
            test=k+a[i+1]+a[i+2]
            if 'R' in test and 'L' in test and 'B' in test:
                res+='C'
                i+=3
            else:
                if k=='R':
                    res+='S'
                elif k=='B':
                    res+='K'
                elif k=='L':
                    res+='H'
                i+=1
        else:
            if k=='R':
                res+='S'
            elif k=='B':
                res+='K'
            elif k=='L':
                res+='H'
            i+=1
            
    sys.stdout.write(res)

main()


# res=''
# a=deque(list(sys.stdin.read()))

# while a:
#     k=a.popleft()
#     if len(a)>1:
#         test=k+a[0]+a[1]
#         if 'R' in test and 'L' in test and 'B' in test:
#             res+='C'
#             a.popleft()
#             a.popleft()
#         else:
#             if k=='R':
#                 res+='S'
#             elif k=='B':
#                 res+='K'
#             elif k=='L':
#                 res+='H'
#     else:
#         if k=='R':
#             res+='S'
#         elif k=='B':
#             res+='K'
#         elif k=='L':
#             res+='H'

# sys.stdout.write(res)