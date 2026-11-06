---
type: source
tags: [year2]
sources: ["[[chp2 - piles listes file]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[chp2 - piles listes file]], dans [[Algo (matière)]]. En cas d'écart, le cours et ses images font foi.

## Idée générale

Chapitre 2 de l'algorithmique de Year 2 : trois structures de données qui rangent des éléments dans un certain ordre, la liste, la pile et la file. Voir [[Pile et file]] et [[Liste chaînée]].

## Résumé comparatif pile / file

| Pile | File |
|---|---|
| Les objets sont insérés et supprimés à une seule extrémité | Les objets sont insérés et retirés aux 2 extrémités (voir point à vérifier 1) |
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

![[Cours/Year 2/Algo/Cours/medias/chp2 - piles listes file/image4.png]]
*Figure : liste 1, 2, 3, 4, 5 ; les cases 1 à 4 forment la queue, la case 5, dernier élément ajouté, est la tête.*

### Liste chaînée

- Contrairement à un [[Tableau (programmation)|tableau]], les éléments d'une [[Liste chaînée|liste chaînée]] ne sont pas à la suite dans la mémoire.
- Chaque élément est toujours accompagné d'un [[Pointeur et adresse mémoire|pointeur]] qui indique où se trouve l'élément suivant dans la mémoire.
- Une liste chaînée est constituée de **chaînons**, une structure qui contient :
  - l'élément à stocker (entier, flottant, tableau de caractères, etc.) ;
  - un pointeur vers l'occurrence suivante.

![[Cours/Year 2/Algo/Cours/medias/chp2 - piles listes file/image6.png]]
*Figure : un chaînon, avec « elm » (élément stocké : entier, réel, structure…) et « \* » (pointeur sur l'élément suivant) ; l'image contient aussi le tableau des opérations ci-dessous.*

### Opérations sur une liste

| Action | Instruction |
|---|---|
| Créer une liste `L` vide | `L = vide()` |
| Tester si la liste `L` est vide | `estVide(L)` |
| Ajouter un élément `x` en tête de la liste `L` | `ajouteEnTete(x,L)` |
| Supprimer la tête `x` d'une liste `L` et renvoyer cette tête | `supprEnTete(L)` |
| Compter le nombre d'éléments de `L` | `compte(L)` |
| Créer une nouvelle liste `L1` à partir d'un élément `x` et d'une liste existante `L` | `L1 = cons(x,L)` |

## Piles

Principe **LIFO** (*last in first out*) : le dernier élément empilé est le premier dépilé.

![[Cours/Year 2/Algo/Cours/medias/chp2 - piles listes file/image1.png]]
*Figure : le long de l'axe du temps $t$, on empile (« Push ») 2, 3 puis 4 sur 1, puis on dépile (« Pop ») 4, 3 puis 2 ; il reste 1.*

Dans la pile, on garde toujours trace du dernier élément présent avec un pointeur appelé **`top`**.

| Action sur la pile | Méthode de la classe *Pile* |
|---|---|
| La pile est-elle vide ? | `estVide()` |
| Empiler un nouvel élément | `empiler(élément)` |
| Dépiler un élément | `depiler()` |
| Lire la valeur au sommet | `lireSommet()` |
| Afficher le nombre d'éléments | `taille()` |

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

## Files

Principe **FIFO** (*first in first out*) : le premier élément enfilé est le premier défilé.

![[Cours/Year 2/Algo/Cours/medias/chp2 - piles listes file/image7.png]]
*Figure : au fil du temps $t$, on enfile (« Enqueue ») 2, 3 et 4 derrière 1, puis on défile (« Dequeue ») 1, 2 puis 3 ; il reste 4.*

Dans la file, il y a deux pointeurs :

- le **pointeur avant**, sur l'élément inséré en premier et toujours présent ;
- le **pointeur arrière**, sur l'élément inséré en dernier.

| Action sur la file | Méthode de la classe *File* |
|---|---|
| Enfiler un nouvel élément | `enfiler(élément)` |
| Défiler | `defiler()` |
| La file est-elle vide ? | `estVide()` |
| Afficher le nombre d'éléments | `longeur()` (sic) |

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Images lues par leur transcription, aucune ouverte.

1. **Tableau pile / file** : la colonne File dit que les objets sont « insérés et retirés aux 2 extrémités ». C'est imprécis : une file insère à une extrémité et retire à l'autre, comme le montre l'illustration enfiler/défiler (complément).
2. **Coquilles signalées par les transcriptions** : « le tète » et `longeur()` sont recopiés tels quels, probablement pour « tête » et `longueur()`.
3. **Aucune implémentation de la file** n'est donnée, ni pour la pile hors de la liste Python.
