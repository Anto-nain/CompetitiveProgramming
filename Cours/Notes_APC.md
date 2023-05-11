# Notes APC

# Chaînes de caractère
## Transformer une chaine de caractère en minuscule

```python
'Aa'.lower()
```

## Transformer une chaine de caractère en majuscule

```python
'Aa'.upper()
```

# Fast I/O
Méthodes bien plus rapides que ```input``` et ```print```
## Fast input
On utilise le document ```.txt``` suivant comme variable d'entrée :
```txt
ligne 1
ligne 2
```

### ```sys.stdin.read```
Cette méthode lit toutes les lignes de l'entrée et les garde sous forme d'une seule chaîne de caractère (avec les sauts de lignes)
```python
import sys
t = sys.stdin.read()
print(t)
print('\n')
print(t.splitlines())
```
Renvoie :
```txt
ligne 1
ligne 2

['ligne 1', 'ligne 2']
```
>Avec la méthode ```splitlines``` on peut facilement récupérer toutes les données

### ```sys.stdin.readlines```

Cette méthode lit toutes les lignes de l'entrée et les sépare sous la forme d'une liste de chaîne de caractère (ligne par ligne)
```python
import sys
t = sys.stdin.readlines()
print(t)
```
Renvoie :
```txt
['ligne 1\n', 'ligne 2']
```
Ici, la présence du `\n` rajoute un caractère "saut de ligne" à la fin des lignes (sauf de la dernière).
>Il faut noter que `\n` ne constitue qu'un seul caractère 
>```python
>t = 'ligne\n'
>print('*')
>print(t[-1])
>print('*')
>```
>Renvoie 
>```txt
>*
>
>
>*
>```
>Avec deux lignes entre les '*'


## Fast output

### ```sys.stdout.write```
Fonctionne exactement comme la fonction ```print``` mais ne prends que des chaînes de caractère en argument.
### ```sys.stdout.writelines```
Fonctionne comme ```sys.stdout.write``` mais peut prendre une liste de chaînes de caractère en argument. La fonction va alors concaténer les chaînes de caractère entre elle et afficher la chaîne créée.

```python
import sys
sys.stdout.writelines(['ab','cd'])
sys.stdout.writelines('ef')
sys.stdout.writelines(['gh\n', 'ij'])
```
Renvoie :
```txt
abcd
ef
gh
ij
```
>Comme on vient de le voir, ```sys.stdout.writelines``` fonctionne bien de paire avec ```sys.stdin.readlines```.

## Les sets

Différents exemples de sets

```python
S1 = set()
S2 = {'chien','chat','hamster'}
```

> Attention à la création d'un set, { } est dictionnaire !!!!


Pour ajouter ou retirer des éléments

```Python
S2.add("cheval")
S2.remove("cheval")
```

> L'avantage d'un set (comme pour un dictionnaire) est que, l'on peut tester la présence d'un élément en O(log(n)) contre O(n) pour une liste

```Python
if "cheval" in S: # O(log(n))
    ...

if "cheval" in L: # O(n)
    ...
```

## Copier une liste

Une liste est un objet stocké avec une adresse spéciale et ne peut pas être copiée simplement par une affectation

Exemple :

```python3
L1 = ['chien','chat','hamster']
L2 = L1
L2[1] = 'cheval'
```

Alors L1 est aussi modifiée et L1[1] est 'cheval'. Pour éviter cela il faut dupliquer correctement la matrice :  
Avec deepcopy (le plus rapide)
```python
from copy import deepcopy
L1 = deepcopy(L2)
```
En créant un nouvel objet avec ```python3``` uniquement :

```python
L1 = [element for element in L2]
```
## Opérations sur les listes
### Trier une liste

Il existe 2 façons de trier une liste L donnée:
```python
L.sort() # modifie L
```
```python
L_trié = sorted(L) # ne modifie pas L
```

> tris en O(nlog(n))

Ces deux manières de trier une liste fonctionnent pour des ```int```, ```float``` et ```str``` (auquel cas on trie les chaînes de caractères par ordre alphabétique). On peut aussi trier des ```tuple``` à condition que les éléments des tuples soient triables. Dans ce cas, on triera d'abord les premier élément du tuple, puis, si égalité, le second et ainsi de suite.