---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF Chapitre4-Preing2ID ([[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]) (63 diapositives, « Chapitre 4 : Les arbres binaires », groupe Preing2 ID, 2024-2025, format beamer avec animations), dans [[Cours/Informatique (cours)/Algo (cours)/Algo (index)]]. Les exemples sont en [[Langage Python|Python]].

## Idée générale

Définir l'[[Arbre binaire]], son vocabulaire et ses propriétés, puis le parcourir et le coder. Le cours insiste sur le gain de temps d'un arbre par rapport aux listes, piles et files (« 10000 ans → quelques secondes »).

## 1. L'arbre comme structure de données

- Il apparaît naturellement : XML, arborescences de répertoires…
- Structure qui permet de ranger efficacement des données.
- Gain de temps spectaculaire par rapport aux listes, [[Pile et file|piles et files]] : « 10000 ans → quelques secondes ».

## 2. Définition

> **Définition récursive.** Un **arbre binaire étiqueté** est :
> - soit l'**arbre vide**, noté `()` ou `Empty` dans ce cours ;
> - soit formé d'un **nœud**, appelé sa **racine**, portant une information appelée **étiquette** du nœud, et de deux arbres binaires, appelés **sous-arbres gauche et droit**.

Un arbre non vide $t$ est donc décrit par un triplet $(v, l, r)$ :

- une valeur $v$ de type fixé, l'étiquette de la racine de $t$ ;
- un arbre $l$, le sous-arbre gauche de $t$ ;
- un arbre $r$, le sous-arbre droit de $t$.

### Représentation graphique

Définition récursive $\Rightarrow$ dessin obtenu récursivement : l'arbre vide est un petit carré ; l'arbre non vide $(v, l, r)$ est un nœud $v$ (la racine) relié à deux triangles $l$ et $r$, et le dessin continue récursivement pour $l$ et $r$.

![[Chapitre4-Preing2ID - p8.jpg]]
*Figure : arbre vide (carré rouge) et arbre non vide $(v, l, r)$ : racine $v$ et sous-arbres $l$, $r$.*

**Attention !** L'arbre vide n'est pas un nœud !

### Exemple

$$t = (\underbrace{1}_{v},\ \underbrace{(42, (), ())}_{l},\ \underbrace{(100, (), (123, (), ()))}_{r})$$

![[Chapitre4-Preing2ID - p9.jpg]]
*Figure : l'arbre $t$ : racine 1, fils gauche 42, fils droit 100 dont le fils droit est 123 ; les sous-arbres vides sont dessinés en carrés.*

### Squelette

Le **squelette** d'un arbre binaire s'obtient en supprimant les étiquettes.

![[Chapitre4-Preing2ID - p10.jpg]]
*Figure : (a) un arbre binaire 1 ; 2 (fils droit 3) ; 4 ; (b) son squelette, mêmes nœuds sans étiquettes.*

Les sous-arbres vides sont inutiles à dessiner :

![[Chapitre4-Preing2ID - p11.jpg]]
*Figure : (a) l'arbre avec ses sous-arbres vides ; (b) le même, sans dessiner les sous-arbres vides.*

## 3. Vocabulaire à connaître

Voir [[Vocabulaire des arbres]]. Les diapositives utilisent toutes le même arbre : 1 a pour fils 2 et 8 ; 2 a pour fils 3 et 7 ; 3 a pour fils 4 et 5 ; 5 a un fils gauche 6 ; 8 a un fils droit 9.

### Sous-arbre enraciné en un nœud $x$

Arbre situé « en dessous du nœud $x$ » ($x$ inclus).

![[Chapitre4-Preing2ID - p13.jpg]]
*Figure : le sous-arbre enraciné en $x = 2$ (encadré) : 2, 3, 7, 4, 5, 6.*

### Fils gauche, fils droit

Le **fils gauche** de $x$, noté $\text{fg}(x)$, est la racine du sous-arbre gauche (de même pour $\text{fd}(x)$).

![[Chapitre4-Preing2ID - p14.jpg]]
*Figure : $x = 2$, $\text{fg}(x) = 3$, $\text{fd}(x) = 7$.*

- Le nœud 5 a un fils gauche mais pas de fils droit.
- Le nœud 8 a un fils droit mais pas de fils gauche.
- Les nœuds 4, 6, 7, 9 n'ont pas de fils.

### Père

Le père d'un fils de $x$ est $x$. Tout nœud sauf la racine a un (seul) père.

![[Chapitre4-Preing2ID - p15.jpg]]
*Figure : $x = 3$ et $\text{pere}(x) = 2$.*

### Arité

Arité d'un nœud $x$ = nombre de fils de $x$.

![[Chapitre4-Preing2ID - p16.jpg]]
*Figure : arités : 1 → 2, 2 → 2, 8 → 1, 3 → 2, 7 → 0, 9 → 0, 4 → 0, 5 → 1, 6 → 0.*

### Feuille

Feuille = nœud dont l'arité est 0.

![[Chapitre4-Preing2ID - p17.jpg]]
*Figure : les feuilles 4, 6, 7, 9 entourées.*

### Arête

Relie un fils et son père.

![[Chapitre4-Preing2ID - p18.jpg]]
*Figure : trois arêtes de l'arbre, en bleu.*

### Branche

Chemin de la racine à une feuille.

![[Chapitre4-Preing2ID - p19.jpg]]
*Figure : la branche 1 → 2 → 7 en rouge.*

- Exemple : $1 \to 2 \to 7$.
- Une branche descend de la racine jusqu'à une feuille.
- Longueur d'une branche = son nombre d'arêtes.

### Hauteur

Hauteur d'un arbre = longueur maximale d'une branche (voir [[Hauteur d'un arbre]]).

![[Chapitre4-Preing2ID - p20.jpg]]
*Figure : la plus longue branche 1 → 2 → 3 → 5 → 6, en rouge : la hauteur est 4.*

### Taille

Taille d'un arbre = nombre de nœuds. L'arbre exemple a pour taille 9.

### Profondeur (ou niveau)

Profondeur d'un nœud = nombre d'arêtes qui le séparent de la racine. Le terme **niveau** est synonyme de **profondeur**.

![[Chapitre4-Preing2ID - p22.jpg]]
*Figure : niveaux : 1 au niveau 0 ; 2, 8 au niveau 1 ; 3, 7, 9 au niveau 2 ; 4, 5 au niveau 3 ; 6 au niveau 4.*

## 4. Arbres binaires particuliers

> Un arbre binaire est :
> - **complet** s'il n'a pas de nœud d'arité 1 ;
> - **parfait** s'il est complet et que toutes les feuilles ont le même niveau ;
> - **quasi-parfait** si :
>   - il est complet jusqu'au niveau $h - 1$,
>   - ses feuilles sont à profondeur $h$ ou $h - 1$,
>   - les feuilles de profondeur $h$ sont « le plus à gauche possible ».
>
> Remarque : tout arbre parfait est quasi-parfait.

![[Chapitre4-Preing2ID - p25.jpg]]
*Figure : à gauche, arbre non complet (le nœud 3 n'a qu'un fils, 5) ; à droite, le même complété par un nœud 4 : arbre complet.*

![[Chapitre4-Preing2ID - p26.jpg]]
*Figure : arbre parfait de hauteur 3, nœuds numérotés de 1 à 15 niveau par niveau.*

![[Chapitre4-Preing2ID - p27.jpg]]
*Figure : arbre quasi-parfait : nœuds 1 à 12, le dernier niveau rempli de gauche à droite jusqu'à 12.*

## 5. Propriétés sur les arbres

- La hauteur, le nombre de nœuds, le nombre de feuilles, etc., vérifient des relations simples.
- Un **objectif de l'UE** : comprendre comment montrer ces relations par [[Récurrence|récurrence]].
- Récurrences : sur la taille ou sur la hauteur des arbres.
- « Pourquoi une preuve formelle et comment rédiger ? »

### Exemple : tout arbre binaire non vide a au moins une feuille

On raisonne par récurrence (forte) sur la taille $n(t) = n$ de l'arbre $t$.

1. Comme $t$ est non vide, $n \ge 1$.
2. Si $n = 1$, la racine de $t$ est une feuille.
3. Supposons le résultat vrai pour tout arbre de taille $\le n - 1$. Soit $t$ de taille $n > 1$.
4. Comme $t$ est formé d'un nœud racine et de sous-arbres $l$ et $r$ :
$$n = 1 + n(l) + n(r) \quad (1)$$
où $n(l)$ et $n(r)$ sont les tailles de $l$ et $r$.
5. Comme $n > 1$, $l$ ou $r$ n'est pas vide, par exemple $l$.
6. D'après (1), $n(l) \le n - 1$.
7. Par hypothèse de récurrence, $l$ a au moins une feuille.
8. Cette feuille est aussi une feuille de $t$.

### Propriétés des arbres binaires

Notations, pour un arbre $t$ : $h(t)$ sa hauteur, $n(t)$ son nombre de nœuds, $i(t)$ son nombre de nœuds internes, $l(t)$ son nombre de feuilles. Question posée : comment calculer récursivement ces paramètres ?

> **Propriétés** (se montrent par récurrence) :
> 1. $h(t) + 1 \le n(t) \le 2^{h(t)+1} - 1$.
> 2. L'arité de tous les nœuds internes de $t$ est 1 si et seulement si $h(t) + 1 = n(t)$.
> 3. L'arbre $t$ est parfait si et seulement si $n(t) = 2^{h(t)+1} - 1$.
> 4. Si $t$ est un arbre complet, $i(t) = l(t) - 1$.

Les démonstrations ne sont pas données.

## 6. Parcours en profondeur

Voir [[Parcours en profondeur]].

- But : effectuer un traitement sur tous les nœuds d'un arbre.
- Se programme très simplement de façon récursive.
- **Postfixe** : parcourir le sous-arbre gauche, puis le sous-arbre droit, puis effectuer le traitement sur la racine.
- **Infixe** : gauche, racine, droite (non détaillé sur la diapositive).
- **Préfixe** : racine, gauche, droite (non détaillé sur la diapositive).

### Exemple : arbre parfait de hauteur 2

![[Chapitre4-Preing2ID - p42.jpg]]
*Figure P2 : arbre parfait de hauteur 2 : 1 ; 2 (3, 4) ; 5 (6, 7).*

Dans quel ordre les nœuds sont-ils traités ?

| Parcours | Ordre |
|---|---|
| Préfixe | 1 2 3 4 5 6 7 |
| Infixe | 3 2 4 1 6 5 7 |
| Postfixe | 3 4 2 6 7 5 1 |

## 7. Implémentation en Python

Classe `ArbreBinaire` (indentation reconstituée) :

```python
class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None

    def insert_gauche(self, valeur):
        if self.enfant_gauche == None:
            self.enfant_gauche = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_gauche = self.enfant_gauche
            self.enfant_gauche = new_node

    def insert_droit(self, valeur):
        if self.enfant_droit == None:
            self.enfant_droit = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_droit = self.enfant_droit
            self.enfant_droit = new_node

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.enfant_gauche

    def get_droit(self):
        return self.enfant_droit
```

Si le fils existe déjà, `insert_gauche` (resp. `insert_droit`) intercale le nouveau nœud : l'ancien fils devient le fils gauche (resp. droit) du nouveau.

## 8. Exercice : coder un arbre binaire

![[Chapitre4-Preing2ID - p48.jpg]]
*Figure : l'arbre de l'exercice : r ; a (c, d) ; b (e, f) ; c a un fils droit h ; d (i, j) ; j a un fils gauche m ; e a un fils gauche k.*

- `r` est la racine, son fils gauche est `a`, son fils droit est `b`.
- `j` a un fils gauche (`m`) et pas de fils droit.
- `m` n'a pas de fils : c'est une feuille.

### Codage par dictionnaires

```python
def noeud(nom, fg=None, fd=None):
    return {'racine': nom, 'fg': fg, 'fd': fd}

k = noeud('k')
f = noeud('f')
e = noeud('e', k, None)
b = noeud('b', e, f)
m = noeud('m')
j = noeud('j', m, None)
i = noeud('i')
d = noeud('d', i, j)
h = noeud('h')
c = noeud('c', None, h)
a = noeud('a', c, d)
A = noeud('r', a, b)
```

### Question 1 : représentation en liste imbriquée

On veut la représentation suivante :

- l'arbre vide est représenté par `[]` ;
- `A = noeud('r')` est représenté par `['r', [], []]` ;
- `b = noeud('b'); a = noeud('a'); A = noeud('r', a, b)` est représenté par `['r', ['a', [], []], ['b', [], []]]` ;
- `c = noeud('c'); b = noeud('b', c, None); a = noeud('a'); A = noeud('r', a, b)` est représenté par `['r', ['a', [], []], ['b', ['c', [], []], []]]`.

Écrire une fonction Python [[Récursivité|récursive]] qui obtient cette liste à partir du codage proposé. Corrigé du cours :

```python
def construit(arbre):
    if arbre == None: return []
    else: return [arbre['racine'], construit(arbre['fg']), construit(arbre['fd'])]

print(construit(A))
```

### Question 2 : hauteur

L'arbre de l'exercice a pour hauteur 4 : c'est la plus grande distance entre la racine et une feuille (r → a → d → j → m). Définir une fonction récursive qui détermine la hauteur d'un arbre. Corrigé du cours :

```python
def hauteur(arbre):
    if arbre == []: return -1
    else:
        h1 = 1 + hauteur(arbre[1])
        h2 = 1 + hauteur(arbre[2])
        return max(h1, h2)

print(hauteur(construit(A)))
```

### Question 3 : parcours

- **Préfixe** : chaque sommet est traité la première fois qu'on le rencontre dans la balade. Ici : r, a, c, h, d, i, j, m, b, e, k, f.
- **Postfixe** : chaque sommet est traité la dernière fois qu'on le rencontre. Ici : h, c, i, m, j, d, a, k, e, f, b, r.
- **Infixe** : ici c, h, a, i, d, m, j, r, k, e, b, f.

Écrire une fonction récursive pour chacun des parcours. Corrigé du cours :

```python
def parcoursPrefixe(arbre):
    if arbre != []:
        print(arbre[0], end=',')
        parcoursPrefixe(arbre[1])
        parcoursPrefixe(arbre[2])

def parcoursPostfixe(arbre):
    if arbre != []:
        parcoursPostfixe(arbre[1])
        parcoursPostfixe(arbre[2])
        print(arbre[0], end=',')

def parcoursInfixe(arbre):
    if arbre != []:
        parcoursInfixe(arbre[1])
        print(arbre[0], end=',')
        parcoursInfixe(arbre[2])

print("Parcours préfixe : ")
parcoursPrefixe(construit(A))
print('\n')
print("Parcours postfixe : ")
parcoursPostfixe(construit(A))
print()
print("\nParcours infixe : ")
parcoursInfixe(construit(A))
```

## Liens

Précédé de [[3 - Arbres (résumé)]], suivi de [[5 - ABR (résumé)]]. Voir aussi [[Récursivité]] et [[Arbre AVL]].

## Points à vérifier

1. **Numérotation des diapositives** : les pieds de page indiquent « x/40 » alors que le PDF compte 63 pages (animations beamer dupliquées, puis diapositives d'exercice non numérotées). Les numéros de figure renvoient aux pages du PDF.
2. **Code de `ArbreBinaire`** : dans le PDF, plusieurs instructions sont collées sur une même ligne (`def __init__(self, valeur): self.valeur = valeur`, `new_node = ArbreBinaire(valeur) new_node.enfant_droit = …`) et `insert_droit`, `get_valeur`, `get_gauche`, `get_droit` sont répétés deux fois. L'indentation donnée ici est reconstituée.
3. **Guillemet typographique** : dans `parcoursPrefixe`, le PDF écrit `end = ',’` avec un guillemet fermant typographique, qui provoquerait une erreur de syntaxe ; corrigé ici en `','`.
4. **Parcours infixe et préfixe** : seule la définition du postfixe est détaillée ; les deux autres ne sont que nommés (complément : préfixe = racine, gauche, droite ; infixe = gauche, racine, droite).
5. **Hauteur d'un arbre vide** : `hauteur([])` renvoie $-1$, cohérent avec le [[3 - Arbres (résumé)|chapitre 3]] mais pas avec [[6 - AVL (résumé)|ARBRE AVL]] ($h(\text{NIL}) = 0$).
6. **Propriétés 1 à 4** : énoncées sans démonstration ; seule la propriété « tout arbre non vide a une feuille » est prouvée.
