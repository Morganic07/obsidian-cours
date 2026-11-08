---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf|Chapitre5-ABR.pdf]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé du PDF Chapitre5-ABR ([[Raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf|Chapitre5-ABR.pdf]]) (30 diapositives, « Chapitre 5 : Les arbres binaires de recherche », ID2, 2024-2025), dans [[Cours/Informatique/Algo/_index|Algo]]. Le code est en [[Langage Python|Python]], en programmation objet ; l'indentation, perdue dans le PDF, est reconstituée.

## Idée générale

Définir l'[[Arbre binaire de recherche]] (ABR) et programmer ses opérations : création, insertion, parcours, recherche, minimum, maximum, suppression.

## 1. Définition

Un **arbre binaire de recherche** est un [[Arbre binaire|arbre binaire]] tel que, pour chacun de ses nœuds :

- chaque nœud du sous-arbre gauche a une clé **inférieure** à celle du nœud considéré ; [[Erreurs du cours#^e-5-abr|✎]]
- chaque nœud du sous-arbre droit a une clé **supérieure** à celle-ci. [[Erreurs du cours#^e-5-abr|✎]]

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

Pourquoi : par récurrence sur la taille. Le parcours infixe d'un ABR $a$ énumère d'abord son sous-arbre gauche (dans l'ordre croissant par hypothèse de récurrence, et toutes ces clés sont inférieures à la racine), puis la racine, puis le sous-arbre droit (dans l'ordre croissant, toutes ces clés supérieures à la racine) : la suite obtenue est croissante. La réciproque est vraie aussi : un arbre binaire est un ABR si et seulement si son parcours infixe est croissant, ce qui donne un moyen simple de **vérifier** qu'un arbre est un ABR. [[Complément hors du cours|ⓘ]]

Attention, il ne suffit pas de vérifier que chaque nœud est plus grand que son fils gauche et plus petit que son fils droit : la condition porte sur **tout** le sous-arbre. Par exemple, l'arbre 10 ; 5 (2, 12) ; 15 respecte la condition entre chaque père et ses fils, mais n'est pas un ABR, car 12 est dans le sous-arbre gauche de 10. [[Complément hors du cours|ⓘ]]

Application, le **tri par ABR** : insérer les $n$ valeurs une à une dans un ABR vide, puis le parcourir en infixe. Le coût est celui des $n$ insertions : de l'ordre de $n \log n$ si l'arbre reste équilibré, mais $n^2/2$ comparaisons environ si les valeurs arrivent déjà triées (voir la section 5). [[Complément hors du cours|ⓘ]]

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

Méthode [[Récursivité|récursive]]. Une valeur égale à celle d'un nœud n'est pas insérée, ce qui correspond aux inégalités strictes de la définition.

Le nouveau nœud est toujours ajouté comme **feuille** : l'insertion ne réorganise jamais l'arbre. La forme de l'ABR dépend donc de l'**ordre d'insertion**. Avec les valeurs 4, 2, 6, 1, 3, 5, 7, on obtient un arbre parfait de hauteur 2 (racine 4 ; 2 (1, 3) ; 6 (5, 7)) ; avec les mêmes valeurs dans l'ordre 1, 2, 3, 4, 5, 6, 7, chaque nœud n'a qu'un fils droit et l'arbre est une « liste » de hauteur 6, dit **dégénéré** (ou filiforme). [[Complément hors du cours|ⓘ]]

## 4. Traverser l'arbre

Traverser l'arbre, c'est visiter tous ses nœuds. Il existe des méthodes générales de parcours de graphe (voir [[Parcours en profondeur]], [[Parcours en largeur]]) et des méthodes propres aux arbres binaires, basées sur la récursivité.

En traversant l'arbre en parcours **infixe** (*in-order*, car il donne les valeurs dans l'ordre croissant) et en gardant trace du niveau, on génère une représentation graphique (arbre couché, droite en haut) : [[Erreurs du cours#^e-5-abr|✎]]

```python
def pprint(self, level=0):
    if self.right:
        self.right.pprint(level + 1)
    print(f"{' ' * 4 * level}{self.data}")
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

**Complexité.** La recherche suit une seule branche, en descendant d'un niveau à chaque comparaison : elle fait au plus $h + 1$ comparaisons, où $h$ est la [[Hauteur d'un arbre|hauteur]] de l'arbre. Il en va de même pour l'insertion, le minimum, le maximum et la suppression : toutes les opérations d'un ABR sont en $O(h)$. Or $h$ est compris entre $\lfloor \log_2 n \rfloor$ (arbre bien rempli, voir les propriétés du [[4 - Arbres binaires|chapitre 4]]) et $n - 1$ (arbre dégénéré) : [[Complément hors du cours|ⓘ]]

| Cas | Hauteur | Coût d'une recherche |
|---|---|---|
| arbre équilibré | $\approx \log_2 n$ | $O(\log n)$, environ 20 comparaisons pour $n = 10^6$ |
| valeurs insérées dans un ordre aléatoire | en moyenne $O(\log n)$ | $O(\log n)$ en moyenne |
| arbre dégénéré (valeurs insérées triées) | $n - 1$ | $O(n)$, comme une liste |

Ce pire cas motive les arbres **équilibrés**, qui garantissent une hauteur en $O(\log n)$ quel que soit l'ordre d'insertion : c'est l'objet de l'[[Arbre AVL]] ([[6 - AVL]]). La recherche dans un ABR équilibré suit la même idée que la [[Recherche dichotomique|recherche dichotomique]] dans un tableau trié, mais l'ABR permet en plus d'insérer et de supprimer sans décaler les éléments. [[Complément hors du cours|ⓘ]]

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

1. Le nœud à supprimer n'a **pas d'enfant** (c'est une feuille) : on le supprime ; si cette feuille est la racine (arbre à un seul nœud), elle n'a pas de parent et l'arbre devient vide. [[Erreurs du cours#^e-5-abr|✎]]
2. Il a **un seul enfant** : on le remplace par son fils.
3. Il a **deux enfants** : on le remplace par son **successeur** (le minimum de son sous-arbre droit).

Pourquoi le successeur convient : c'est la plus petite valeur supérieure à celle du nœud supprimé. Placé à sa place, il reste plus grand que tout le sous-arbre gauche et plus petit que tout ce qui reste du sous-arbre droit : la propriété d'ABR est préservée. De plus, étant le nœud le plus à gauche du sous-arbre droit, il n'a **pas de fils gauche** : le retirer de sa position d'origine relève du cas 1 ou du cas 2, ce que fait la fin du code (`succ.parent.left = succ.right`). On peut symétriquement utiliser le **prédécesseur**, le maximum du sous-arbre gauche. [[Complément hors du cours|ⓘ]]

Exemple sur le premier ABR de la section 1 (racine 7 ; 4 (2, 6) ; 11 (9 (8, 10), 12)) : pour supprimer 7, qui a deux enfants, on cherche le minimum du sous-arbre droit, 8 ; on recopie 8 à la racine, puis on retire l'ancien nœud 8, qui est une feuille. [[Complément hors du cours|ⓘ]]

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
        elif node.is_right_child():
            node.parent.right = None
        else:
            # la feuille est la racine : l'arbre devient vide
            node.data = None
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

Une façon de les écrire, dans la classe `Node`, pour que `delete` fonctionne (`get_successor` n'est appelée ici que sur un nœud à deux enfants, dont le successeur est le minimum du sous-arbre droit) : [[Complément hors du cours|ⓘ]]

```python
def count_children(self):
    return (self.left is not None) + (self.right is not None)

def is_left_child(self):
    return self.parent is not None and self.parent.left is self

def is_right_child(self):
    return self.parent is not None and self.parent.right is self

def get_successor(self):
    return self.right.min()
```

En Python, `del node` ne détruit pas le nœud : il supprime seulement le nom local `node`. Le nœud disparaît parce que plus rien ne pointe vers lui (son père ne le référence plus), et le ramasse-miettes de Python libère alors sa mémoire. [[Complément hors du cours|ⓘ]]

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

Le cours ne donne pas de corrigé.

Pour vérifier son dessin : c'est l'arbre de l'expression $(3 + 4/2) \times (8 - 2 \times 3)$, de hauteur 3 (racine de hauteur 0 au sens du [[3 - Arbres|chapitre 3]]). Voir [[Hauteur d'un arbre]]. [[Complément hors du cours|ⓘ]]

Les trois affichages demandés, pour se corriger : [[Complément hors du cours|ⓘ]]
- préfixe : `* + 3 / 4 2 - 8 * 2 3` ;
- infixe : `3 + 4 / 2 * 8 - 2 * 3` ;
- postfixe : `3 4 2 / + 8 2 3 * - *`.

Ce n'est pas un ABR mais un **arbre d'expression** : les feuilles sont les nombres, les nœuds internes les opérateurs, et l'évaluation se fait en postfixe (on calcule les deux sous-arbres avant d'appliquer l'opérateur) : $(3 + 2) \times (8 - 6) = 10$. L'exercice montre pourquoi on demande « sans parenthèses » : les écritures préfixe et postfixe, appelées [[Notation polonaise|notation polonaise]] et notation polonaise inverse, se lisent sans ambiguïté sans parenthèses, alors que l'infixe sans parenthèses se lirait $3 + (4/2) \times 8 - 2 \times 3 = 13$, ce qui n'est pas l'expression de l'arbre. La notation polonaise inverse s'évalue avec une simple [[Pile et file|pile]] (calculatrices HP, langage PostScript). [[Complément hors du cours|ⓘ]]

## Liens

Précédé de [[4 - Arbres binaires]]. Le cours suivant, l'[[Arbre AVL]], rééquilibre l'ABR (voir [[6 - AVL]]). Pour l'[[Arbre binaire]] et ses parcours, voir le concept.
