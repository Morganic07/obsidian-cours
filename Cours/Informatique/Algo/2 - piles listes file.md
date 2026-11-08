---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/Cours/chp2 - piles listes file.docx|chp2 - piles listes file]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Algo/Cours/chp2 - piles listes file.docx|chp2 - piles listes file]], dans [[Cours/Informatique/Algo/_index|Algo]].
## Idée générale

Chapitre 2 de l'algorithmique de Year 2 : trois structures de données qui rangent des éléments dans un certain ordre, la liste, la pile et la file. Voir [[Pile et file]] et [[Liste chaînée]].

## Résumé comparatif pile / file

| Pile | File |
|---|---|
| Les objets sont insérés et supprimés à une seule extrémité | Les objets sont insérés et retirés aux 2 extrémités : insérés à une extrémité, retirés à l'autre, comme le montre l'illustration enfiler/défiler |
| Un seul pointeur, qui pointe vers le haut de la pile | Deux pointeurs pour les extrémités : la tête et la fin |
| Le dernier objet inséré est le premier à sortir | L'objet inséré en premier est le premier supprimé |
| Ordre *Last In First Out* (**LIFO**) | Ordre *First In First Out* (**FIFO**) |
| Opérations « **Empiler** » et « **Dépiler** » | Opérations « **Enfiler** » et « **Défiler** » |
| Visualisée comme une collection verticale | Visualisée comme une collection horizontale |

## Listes

- Une liste est composée d'éléments **de même nature**, qui possèdent un **rang**.
- On peut supprimer ou ajouter n'importe quel élément.
- Une liste `L` a deux parties :
  - sa **tête**, le dernier élément ajouté à la liste ;
  - sa **queue**, le reste de la liste.

![[chp2 - piles listes file - image4.png]]
*Figure : liste 1, 2, 3, 4, 5 ; les cases 1 à 4 forment la queue, la case 5, dernier élément ajouté, est la tête.*

### Liste chaînée

- Contrairement à un [[Tableau (programmation)|tableau]], les éléments d'une [[Liste chaînée|liste chaînée]] ne sont pas à la suite dans la mémoire.
- Chaque élément est toujours accompagné d'un [[Pointeur et adresse mémoire|pointeur]] qui indique où se trouve l'élément suivant dans la mémoire.
- Une liste chaînée est constituée de **chaînons**, une structure qui contient :
  - l'élément à stocker (entier, flottant, tableau de caractères, etc.) ;
  - un pointeur vers l'occurrence suivante.

![[chp2 - piles listes file - image6.png]]
*Figure : un chaînon, avec « elm » (élément stocké : entier, réel, structure…) et « \* » (pointeur sur l'élément suivant) ; l'image contient aussi le tableau des opérations ci-dessous.*

Le dernier chaînon pointe vers « rien » (`NULL` en C, `None` en Python, voir [[Pointeur NULL]]) : c'est ainsi qu'on reconnaît la fin de la liste. La liste elle-même n'est connue que par un pointeur sur son premier chaînon. [[Complément hors du cours|ⓘ]]

Ce choix de stockage change le coût des opérations par rapport à un tableau : [[Complément hors du cours|ⓘ]]

| Opération | Tableau | Liste chaînée |
|---|---|---|
| Lire le $k$-ième élément | $O(1)$ : on calcule son adresse | $O(k)$ : il faut suivre $k$ pointeurs depuis la tête |
| Ajouter ou supprimer en tête | $O(n)$ : on décale tous les éléments | $O(1)$ : on change un pointeur |
| Insérer après un chaînon déjà repéré | $O(n)$ | $O(1)$ |
| Mémoire | taille fixée à l'avance, cases contiguës | un pointeur en plus par élément, mais la liste grandit à la demande |

En Python, qui n'a pas de pointeurs explicites, un chaînon s'écrit comme un objet qui garde une référence vers le suivant : [[Complément hors du cours|ⓘ]]

```python
class Chainon:
    def __init__(self, elm, suivant=None):
        self.elm = elm            # l'élément stocké
        self.suivant = suivant    # le chaînon suivant, ou None en fin de liste

L = Chainon(3, Chainon(2, Chainon(1)))   # liste 3 → 2 → 1, de tête 3
```

Variantes classiques : la liste **doublement chaînée**, où chaque chaînon pointe aussi vers le précédent (on la parcourt dans les deux sens et l'on supprime un chaînon en $O(1)$), et la liste **circulaire**, où le dernier chaînon pointe vers le premier. Voir [[Liste chaînée]]. [[Complément hors du cours|ⓘ]]

### Opérations sur une liste

| Action | Instruction |
|---|---|
| Créer une liste `L` vide | `L = vide()` |
| Tester si la liste `L` est vide | `estVide(L)` |
| Ajouter un élément `x` en tête de la liste `L` | `ajouteEnTete(x,L)` |
| Supprimer la tête `x` d'une liste `L` et renvoyer cette tête | `supprEnTete(L)` |
| Compter le nombre d'éléments de `L` | `compte(L)` |
| Créer une nouvelle liste `L1` à partir d'un élément `x` et d'une liste existante `L` | `L1 = cons(x,L)` |

Ces opérations font de la liste une structure **récursive** : une liste est soit vide, soit `cons(x, L)`, une tête suivie d'une liste plus courte (le nom `cons`, pour *construct*, vient du langage Lisp). Les fonctions sur les listes s'écrivent alors comme au [[1 - récursivité et complexité|chapitre 1]], avec la liste vide pour condition d'arrêt. Par exemple, en notant `queue(L)` la liste privée de sa tête : `compte(L)` vaut 0 si `estVide(L)`, et `1 + compte(queue(L))` sinon. Voir [[Récursivité]]. [[Complément hors du cours|ⓘ]]

## Piles

Principe **LIFO** (*last in first out*) : le dernier élément empilé est le premier dépilé.

![[chp2 - piles listes file - image1.png]]
*Figure : le long de l'axe du temps $t$, on empile (« Push ») 2, 3 puis 4 sur 1, puis on dépile (« Pop ») 4, 3 puis 2 ; il reste 1.*

Dans la pile, on garde toujours trace du dernier élément présent avec un pointeur appelé **`top`**.

| Action sur la pile | Méthode de la classe *Pile* |
|---|---|
| La pile est-elle vide ? | `estVide()` |
| Empiler un nouvel élément | `empiler(élément)` |
| Dépiler un élément | `depiler()` |
| Lire la valeur au sommet | `lireSommet()` |
| Afficher le nombre d'éléments | `taille()` |

Les piles sont partout dès qu'il faut revenir en arrière dans l'ordre inverse : [[Complément hors du cours|ⓘ]]
- la [[Pile d'exécution|pile d'exécution]] des appels de fonctions, dont la pile de récursion du [[1 - récursivité et complexité|chapitre 1]] ;
- la fonction « Annuler » (Ctrl+Z) d'un éditeur et le bouton « Précédent » d'un navigateur ;
- la vérification des parenthèses d'une expression : on empile chaque `(` et l'on dépile à chaque `)` ; l'expression est bien parenthésée si l'on ne dépile jamais une pile vide et si la pile est vide à la fin ;
- l'évaluation d'une expression en notation polonaise inverse (`3 4 + 2 ×`) : on empile les nombres, et chaque opérateur dépile ses deux opérandes puis empile le résultat ;
- le [[Parcours en profondeur|parcours en profondeur]] d'un arbre ou d'un graphe, écrit sans récursivité.

### Pile en Python

En [[Langage Python|Python]], une liste suffit pour définir une pile, par exemple contenant 1, 3, 5, 7 :

- `[]` est la liste vide ;
- `L.append(x)` ajoute `x` à la fin de `L` (empiler) ;
- `x = L.pop()` renvoie le dernier élément d'une liste non vide et le retire de `L` (dépiler).

```python
# création de la pile P=[1,3,5,7]
P = []
for k in range(4):
    P.append(2*k+1)
```

`append` et `pop()` agissent sur la fin de la liste Python et coûtent $O(1)$ (en moyenne, quand la liste doit parfois être agrandie) : la fin de la liste joue le rôle de `top`. Dépiler une pile vide lève l'erreur `IndexError: pop from empty list` : on teste `estVide()` avant de dépiler. [[Complément hors du cours|ⓘ]]

La classe *Pile* du tableau peut s'écrire ainsi, autour d'une liste Python : [[Complément hors du cours|ⓘ]]

```python
class Pile:
    def __init__(self):
        self.contenu = []
    def estVide(self):
        return len(self.contenu) == 0
    def empiler(self, element):
        self.contenu.append(element)
    def depiler(self):
        return self.contenu.pop()      # erreur si la pile est vide
    def lireSommet(self):
        return self.contenu[-1]        # lit sans retirer
    def taille(self):
        return len(self.contenu)
```

## Files

Principe **FIFO** (*first in first out*) : le premier élément enfilé est le premier défilé.

![[chp2 - piles listes file - image7.png]]
*Figure : au fil du temps $t$, on enfile (« Enqueue ») 2, 3 et 4 derrière 1, puis on défile (« Dequeue ») 1, 2 puis 3 ; il reste 4.*

Dans la file, il y a deux pointeurs :

- le **pointeur avant**, sur l'élément inséré en premier et toujours présent ;
- le **pointeur arrière**, sur l'élément inséré en dernier.

| Action sur la file | Méthode de la classe *File* |
|---|---|
| Enfiler un nouvel élément | `enfiler(élément)` |
| Défiler | `defiler()` |
| La file est-elle vide ? | `estVide()` |
| Afficher le nombre d'éléments | `longueur()` [[Erreurs du cours#^e-2-piles-listes-file\|✎]] |

Usages typiques des files, dès qu'il faut servir dans l'ordre d'arrivée : file d'impression, tampon de données entre un producteur et un consommateur ([[Tampon (buffer)]]), file des processus prêts dans l'[[Ordonnancement des processus|ordonnancement]] d'un système d'exploitation, et [[Parcours en largeur|parcours en largeur]] d'un arbre ou d'un graphe. [[Complément hors du cours|ⓘ]]

### File en Python

Une liste Python fait une mauvaise file : `L.pop(0)` retire le premier élément mais décale tous les autres, soit $O(n)$ à chaque défilement. On utilise plutôt `deque` (*double-ended queue*) du module `collections`, qui ajoute et retire aux deux bouts en $O(1)$ : [[Complément hors du cours|ⓘ]]

```python
from collections import deque

F = deque()        # file vide
F.append(1)        # enfiler 1
F.append(2)        # enfiler 2
x = F.popleft()    # défiler : x vaut 1, il reste 2
len(F)             # nombre d'éléments : 1
```
