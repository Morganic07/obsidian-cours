---
type: source
tags: [year2]
sources: [".raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf"]
maj: 2026-11-06
complet: true
---

Résumé du PDF Chapitre5-ABR (`.raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf`) (30 diapositives, « Chapitre 5 : Les arbres binaires de recherche », ID2, 2024-2025), dans [[Algo (matière)]]. Le code est en [[Langage Python|Python]], en programmation objet ; l'indentation, perdue dans le PDF, est reconstituée.

## Idée générale

Définir l'[[Arbre binaire de recherche]] (ABR) et programmer ses opérations : création, insertion, parcours, recherche, minimum, maximum, suppression.

## 1. Définition

Un **arbre binaire de recherche** est un [[Arbre binaire|arbre binaire]] tel que, pour chacun de ses nœuds :

- chaque nœud du sous-arbre gauche a une clé **inférieure (ou égale)** à celle du nœud considéré ;
- chaque nœud du sous-arbre droit a une clé **supérieure (ou égale)** à celle-ci.

Autrement dit, pour un arbre $a$ :

- les valeurs du sous-arbre de gauche sont $<$ racine$(a)$ ;
- les valeurs du sous-arbre de droite sont $>$ racine$(a)$ ;
- tout sous-arbre de $a$ est un ABR.

Propriété résumée : **Clé.fils-Gauche < Clé.parent < Clé.fils-Droit**.

![[Chapitre5-ABR - p4.jpg]]
*Figure : ABR de racine 7 : à gauche les nœuds de valeurs < 7 (4, 2, 6), à droite les nœuds de valeurs > 7 (11, 9, 12, 8, 10).*

![[Chapitre5-ABR - p5.jpg]]
*Figure : exemples d'ABR : C avec A et D ; 14 avec 10 (8, 11) et 16 (15, 18) ; 14 avec 10 (8, 11) et 16 (15).*

### Exercice : compléter l'arbre

![[Chapitre5-ABR - p6.jpg]]
*Figure : ABR à compléter : 15 ; 10 (5, ?) ; 30 (?, 50) ; 50 (?, ?) ; le fils gauche de 50 a deux fils inconnus.*

![[Chapitre5-ABR - p7.jpg]]
*Figure : une solution : 15 ; 10 (5, 12) ; 30 (20, 50) ; 50 (40, 55) ; 40 (35, 45).*

### Parcours infixe

**À noter !** Le parcours *InOrdre* (infixe) visite les clés dans l'**ordre croissant**.

![[Chapitre5-ABR - p9.jpg]]
*Figure : ABR 14 ; 10 (8, 11) ; 16 (15, 18) ; le parcours infixe visite 8, 10, 11, 14, 15, 16, 18.*

## 2. Créer l'arbre

Un ABR est composé de nœuds. Chaque nœud contient obligatoirement une valeur, et optionnellement un parent et 2 enfants (un à droite, un à gauche). `__init__()` et `__str__()` sont des [[Méthode spéciale Python|méthodes spéciales]] de Python.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)
```

## 3. Insérer un nœud

Lors de l'ajout d'un nœud, il faut respecter les propriétés de l'arbre. On compare la valeur à insérer aux valeurs des nœuds existants en commençant par la racine. Pour chaque nœud, si la valeur à insérer est inférieure, on continue en descendant à gauche, sinon à droite. Le dernier nœud inspecté sera le **parent** du nœud ajouté : si la valeur est plus petite que celle du parent, le nœud devient son fils gauche, sinon son fils droit.

```python
def insert(self, data):
    if data < self.data:
        if self.left is None:
            self.left = Node(data)
            self.left.parent = self
        else:
            self.left.insert(data)
    elif data > self.data:
        if self.right is None:
            self.right = Node(data)
            self.right.parent = self
        else:
            self.right.insert(data)
```

Méthode [[Récursivité|récursive]]. Une valeur égale à celle d'un nœud n'est pas insérée (voir point à vérifier 1).

## 4. Traverser l'arbre

Traverser l'arbre, c'est visiter tous ses nœuds. Il existe des méthodes générales de parcours de graphe (voir [[Parcours en profondeur]], [[Parcours en largeur]]) et des méthodes propres aux arbres binaires, basées sur la récursivité.

En traversant l'arbre en parcours **infixe** (*in-order*, car il donne les valeurs dans l'ordre croissant) et en gardant trace du niveau, on génère une représentation graphique (arbre couché, droite en haut) :

```python
def pprint(self, level=0):
    if self.right:
        self.right.pprint(level + 1)
    print(f"{' ' * 4 * level}{self.data}")   # le PDF écrit ' ' * * level
    if self.left:
        self.left.pprint(level + 1)
```

## 5. Rechercher un nœud

Pour trouver le nœud qui correspond à une valeur, on la compare à celle des nœuds en partant de la racine et en respectant les propriétés de l'arbre, jusqu'à trouver le bon nœud.

```text
rechercher(racine, x)
comparer x à la clé de racine :
  - si x = clé : return
  - si x < clé : chercher dans G
  - si x > clé : chercher dans D
chercher de la même manière dans G ou D
```

![[Chapitre5-ABR - p17.jpg]]
*Figure : recherche dans l'ABR 14 ; 10 (8, 11) ; 16 (15) : $x = 8$ est trouvé, $x = 17$ ne l'est pas.*

```python
def get(self, data):
    if data < self.data:
        return self.left.get(data) if self.left else None
    elif data > self.data:
        return self.right.get(data) if self.right else None
    return self
```

## 6. Minimum et maximum

D'après les propriétés de l'arbre, le nœud de plus petite valeur est forcément **le plus à gauche possible** ; le maximum, **le plus à droite possible**.

```python
def min(self):
    node = self
    while node.left:
        node = node.left
    return node

def max(self):
    node = self
    while node.right:
        node = node.right
    return node
```

## 7. Supprimer un nœud

Trois possibilités principales :

1. Le nœud à supprimer n'a **pas d'enfant** (c'est une feuille) : on le supprime.
2. Il a **un seul enfant** : on le remplace par son fils.
3. Il a **deux enfants** : on le remplace par son **successeur** (le minimum de son sous-arbre droit).

```python
def delete(self, data):
    node = self.get(data)
    if not node:
        return
    children_count = node.count_children()

    if children_count == 0:
        # cas 1 : feuille
        if node.is_left_child():
            node.parent.left = None
        else:
            node.parent.right = None
        del node

    elif children_count == 1:
        # cas 2 : un seul enfant
        child = node.left or node.right
        if node.is_left_child():
            node.parent.left = child
            child.parent = node.parent
            del node
        elif node.is_right_child():
            node.parent.right = child
            child.parent = node.parent
            del node
        else:
            # le nœud est la racine : on recopie l'enfant dans la racine
            root = node
            root.data = child.data
            root.left = child.left
            root.right = child.right
            if child.left:
                child.left.parent = root
            if child.right:
                child.right.parent = root
            del child

    else:
        # cas 3 : deux enfants, remplacement par le successeur
        succ = node.get_successor()
        node.data = succ.data
        if succ.is_left_child():
            succ.parent.left = succ.right
        else:
            succ.parent.right = succ.right
        if succ.right:
            succ.right.parent = succ.parent
        del succ
```

Les méthodes `count_children`, `is_left_child`, `is_right_child` et `get_successor` sont utilisées mais pas définies dans le cours.

## 8. Exercice 1

Considérer l'arbre donné par le tableau suivant (0 : pas de fils) :

| No | Contenu | Gauche | Droite |
|---|---|---|---|
| 1 | `*` | 2 | 3 |
| 2 | `+` | 4 | 5 |
| 3 | `-` | 6 | 7 |
| 4 | 3 | 0 | 0 |
| 5 | `/` | 8 | 9 |
| 6 | 8 | 0 | 0 |
| 7 | `*` | 10 | 11 |
| 8 | 4 | 0 | 0 |
| 9 | 2 | 0 | 0 |
| 10 | 2 | 0 | 0 |
| 11 | 3 | 0 | 0 |

1. Dessiner cet arbre.
2. Quelle est la hauteur de l'arbre ?
3. L'afficher de manière préfixe, puis infixe, puis postfixe, sans parenthèses.

Le cours ne donne pas de corrigé. Pour vérifier son dessin (complément, non issu du cours) : c'est l'arbre de l'expression $(3 + 4/2) \times (8 - 2 \times 3)$, de hauteur 3 (racine de hauteur 0 au sens du [[Chapitre3-Arbres (résumé)|chapitre 3]]). Voir [[Hauteur d'un arbre]].

## Liens

Précédé de [[Chapitre4-Preing2ID (résumé)]]. Le cours suivant, l'[[Arbre AVL]], rééquilibre l'ABR (voir [[ARBRE AVL (résumé)]]). Pour l'[[Arbre binaire]] et ses parcours, voir le concept.

## Points à vérifier

1. **Définition avec et sans égalité** : la première diapositive autorise « inférieure (ou égale) » et « supérieure (ou égale) », la deuxième écrit des inégalités strictes, et le code de `insert` ignore les valeurs égales. Les doublons ne sont pas traités de façon cohérente.
2. **`pprint`** : le PDF écrit `' ' * * level`, qui est une erreur de syntaxe ; il manque sans doute un nombre d'espaces (`' ' * 4 * level` ou `' ' * level`).
3. **`delete`, feuille racine** (complément) : si l'arbre n'a qu'un nœud, `node.parent` vaut `None` et le cas 1 plante ; le cours ne traite la racine que dans le cas à un enfant.
4. **`del node`** (complément) : en Python, `del` ne supprime que le nom local ; c'est la mise à jour des liens du parent qui retire réellement le nœud.
5. **Exercice 1** : l'arbre donné est un arbre d'expression, pas un ABR, alors qu'il clôt le chapitre sur les ABR ; il porte surtout sur les parcours.
6. **Découpage du code** : `delete` est réparti sur neuf diapositives ; l'enchaînement `if` / `elif` / `else` reconstitué ici suit l'ordre des diapositives et doit être relu avec le PDF.
