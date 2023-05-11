T = int(input())

for t in range(T):
    alpahbet = list(input().split())
    N = int(input())
    set_word_seen = set()
    
    id_A = ord('A')
    
    for i in range(N):
        word = input()
        trans_word = []
        for letter in word:
            trans_word.append(alpahbet[ord(letter) - id_A])
        set_word_seen.add(''.join(trans_word))
    
    if len(set_word_seen) != N:
        print('Case #'+str(t+1)+':' + ' YES')
    else:
        print('Case #'+str(t+1)+':' + ' NO')