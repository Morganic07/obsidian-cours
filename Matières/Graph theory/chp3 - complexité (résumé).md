---
type: source
tags: [year4]
sources: ["[[chp3 - complexité]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[chp3 - complexité]], dans [[Graph theory (matière)]]. Cours en français. En cas d'écart, le cours et ses images font foi. Images non ouvertes : toutes contiennent du texte, du code ou des formules, recopiés ici d'après leur transcription. Voir [[Complexité algorithmique]].

## Idée générale

Mesurer le coût d'un algorithme en nombre d'opérations élémentaires et en mémoire, selon la taille $n$ du problème et indépendamment de la machine et du langage.

## Généralités sur la complexité

1. **Complexité temporelle** : nombre d'**opérations élémentaires** qui composent l'algorithme. Une opération élémentaire a un **coût constant**, et toutes sont considérées **à égalité de coût**. Exemples : affectation, addition, multiplication, comparaison.
2. **Complexité spatiale** : taille de la **mémoire** nécessaire pour stocker les structures de données utilisées pendant l'exécution.

Le nombre d'opérations ou la taille mémoire se calcule **en fonction de la taille du problème**, notée $n$ (pour le tri d'un tableau, $n$ = nombre d'éléments), et **indépendamment** de la machine et du langage de programmation.

**Notations :**
- $A$ : un algorithme ;
- $D(n)$ : l'ensemble des données de taille $n$ ;
- $P(d)$ : la probabilité de la donnée $d$ ;
- $\text{Coût}_A(d)$ : le coût de l'algorithme $A$ pour la donnée $d$.

On distingue **pire cas**, **meilleur cas** et **cas moyen** (pondéré par $P(d)$).

## Calculs de complexité

### Exemple : une fonction avec conditionnelle

```python
def f(x, y):
    if x > y:
        h = x * x
    else:
        h = y * y + 1
    return h
```

Le test compte **une comparaison**. La première branche : une opération arithmétique et une affectation (2) ; la seconde : deux opérations arithmétiques et une affectation (3). Le maximum des coûts des alternatives est 3. D'où :

| Cas | $T(n)$ |
|---|---|
| Pire | 4 |
| Meilleur | 3 |
| Moyen | 3,5 |

### Exemple : deux sommes

Selon la note, « ces deux programmes font la même chose, sauf que le premier est en $O(n)$ et le second en $O(1)$ » (voir Points à vérifier, 2).

```python
def somme_1(n):          # somme des n premiers nombres, par une boucle
    S = 0
    for i in range(n):
        S = S + i
    return S

def somme_2(n):          # par la formule
    S = n * (n + 1) // 2
    return S
```

Voir [[Somme des premiers entiers]].

## Notations asymptotiques

**Borne supérieure asymptotique** :
$$O(g(n)) = \{ f : \mathbb{N} \to \mathbb{R}^+ \mid \exists k > 0,\ \exists n_0 \ge 0,\ \forall n \ge n_0,\ 0 \le f(n) \le k \cdot g(n) \}$$
Si $f(n) \in O(g(n))$, $g(n)$ est une borne supérieure asymptotique de $f(n)$, ou $g(n)$ **domine** $f(n)$ ; on note abusivement $f(n) = O(g(n))$.

**Borne inférieure asymptotique** :
$$\Omega(g(n)) = \{ f : \mathbb{N} \to \mathbb{R}^+ \mid \exists k > 0,\ \exists n_0 \ge 0,\ \forall n \ge n_0,\ 0 \le k \cdot g(n) \le f(n) \}$$
On note abusivement $f(n) = \Omega(g(n))$.

**Borne asymptotique (serrée)** :
$$\Theta(g(n)) = \{ f : \mathbb{N} \to \mathbb{R}^+ \mid \exists k_1 > 0,\ k_2 > 0,\ n_0 \ge 0,\ \forall n \ge n_0,\ 0 \le k_1 g(n) \le f(n) \le k_2 g(n) \}$$
On note abusivement $f(n) = \Theta(g(n))$.

### Classes de complexité

Voir [[Classe de complexité]].

| $O$ | Classe |
|---|---|
| $1$ | constant |
| $\log n$ | logarithmique |
| $n$ | linéaire |
| $n \log n$ | quasi-linéaire |
| $n^2$ | quadratique |
| $n^3$ | cubique |
| $2^n$ | exponentiel |
| $n!$ | factoriel |

## Exemples d'algorithmes itératifs

### Quatre boucles `while`

```python
def Algorithm_A:
    i = 1
    j = 1
    while (i <= m) and (j <= n):
        i = i + 1
        j = j + 1
```
Le nombre d'opérations correspond à $\min(m, n)$ : **$O(\min(m, n))$** (« linéaire »).

```python
def Algorithm_B:
    i = 1
    j = 1
    while (i <= m) or (j <= n):
        i = i + 1
        j = j + 1
```
**$O(\max(m, n))$** (« linéaire »).

```python
def Algorithm_C:
    i = 1
    j = 1
    while (j <= n):
        if i <= m:
            i = i + 1
        else:
            j = j + 1
```
**$O(m + n)$** (« linéaire »).

```python
def Algorithm_D:
    i = 1
    j = 1
    while (j <= n):
        if i <= m:
            i = i + 1
        else:
            j = j + 1
            i = 1
```
**$O(m \cdot n)$** (« linéaire » selon la note : voir Points à vérifier, 1).

(Les codes sont écrits `def Algorithm_A :` sans parenthèses dans le cours : du pseudo-code à la syntaxe Python.)

### Recherche séquentielle d'une valeur dans un tableau

Voir [[Recherche séquentielle]].
- **Pire cas** : $x$ ne figure pas dans le tableau ; $n$ itérations : $T(n) = O(n)$.
- **Meilleur cas** : $x$ est le premier élément : $T(n) = O(1)$.
- **Cas moyen** : données réparties avec la probabilité $\frac{1}{n}$ :
$$T(n) = \sum_{i=1}^{n} \frac{1}{n} \cdot i = \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{n+1}{2}, \quad\text{donc } T(n) = O(n).$$

### Recherche dichotomique dans un tableau trié

Voir [[Recherche dichotomique]].

```python
def recherche_dic(x, t):
    d = 0
    f = len(t) - 1
    while (d <= f):
        m = (d + f) // 2
        if t[m] == x:
            return 0
        if t[m] < x:
            d = m + 1
        else:
            f = m - 1
    return -1
```

**Analyse.** On suppose $n = 2^k$ ($k$ entier positif). Soit $v_n$ le nombre maximal d'itérations de la boucle.
- Pour $n = 1$ : $v_1 = 1$.
- Pour $n = 2^k$, $k > 0$ : le tableau est divisé en deux sous-tableaux d'au plus $2^{k-1}$ éléments, donc
$$v_{2^k} \le 1 + v_{2^{k-1}}, \qquad\text{d'où}\qquad v_{2^k} \le k + v_{2^0}.$$
- Donc $T(n) = O(\log_2 n) = O(\log n)$.

Si $n$ n'est pas une puissance de 2, on l'**encadre entre deux puissances de 2** et on refait le raisonnement sur chacune.

### Tri de sélection non récursif

Voir [[Tri par sélection]].

```python
def triSelection(t):
    n = len(t)
    for i in range(n - 1):
        indMini = i
        for j in range(i + 1, n):
            if t[j] < t[indMini]:
                indMini = j
        if i != indMini:
            x = t[i]
            t[i] = t[indMini]
            t[indMini] = x
```

On ne compte que les instructions colorées dans le cours : en rouge, celles de la boucle externe (`indMini = i`, le test `i != indMini` et les trois affectations de l'échange, soit 5) ; en vert, celles de la boucle interne (le test et `indMini = j`, soit 2).

**Pire cas** : tableau trié dans l'ordre décroissant.
$$T(n) = 5(n-1) + \sum_{i=1}^{n-1} 2i = 5(n-1) + \frac{2n(n-1)}{2} = 5n - 5 + n^2 - n = n^2 + 4n - 5.$$
Donc $T(n) = O(n^2)$.

### Tri d'insertion non récursif

**Exercice** : écrire une fonction Python de [[Tri par insertion|tri par insertion]] et étudier sa complexité. La note ne donne pas de correction.

### Produit matriciel

On considère deux matrices $A$ et $B$ de dimensions $(m, n)$ et $(n, p)$. Le [[Produit matriciel|produit]] de $A$ par $B$ est une matrice $C$ (de dimension $(m, p)$, voir Points à vérifier, 3) définie par
$$C_{i,j} = \sum_{k=1}^{n} A_{i,k} \cdot B_{k,j}.$$

La note s'arrête là, sans calcul de complexité.

## Complexité des algorithmes récursifs

Un algorithme récursif décompose un problème en **sous-problèmes de même nature**, puis recompose leurs solutions. La **complexité d'un algorithme récursif est une suite définie par récurrence** (voir [[Calcul de complexité et théorème de résolution]] et [[Récursivité]]).

### Factorielle récursive

```python
def factorielleRecursive(n):
    if n == 0:
        return 1
    else:
        return n * factorielleRecursive(n - 1)
```

- Si $n = 0$ : une seule comparaison, $T(0) = 1$.
- Si $n > 0$ : une comparaison, une multiplication et une soustraction, plus l'appel récursif :
$$T(n) = T(n-1) + 3.$$

Résolution de la [[Suite arithmétique|suite arithmétique]] : $T(n) = 3n + 1$, donc $T(n) = \Theta(n)$ : algorithme **linéaire**. Voir [[Factorielle]].

### Tours de Hanoï

Voir [[Tours de Hanoï]].

```python
def hanoi(de, vers, via, n):
    if n == 1:
        print(de, "vers", vers)
    else:
        hanoi(de, via, vers, n - 1)
        print(de, "vers", vers)
        hanoi(via, vers, de, n - 1)
```

- Si $n = 1$ : une comparaison (on ignore le coût de l'affichage), $T(1) = 1$.
- Si $n > 1$ : un test et deux appels récursifs sur $n - 1$ :
$$T(n) = 2T(n-1) + 1.$$

Résolution par substitutions successives :
$$\begin{aligned}
T(n) &= 2T(n-1) + 1\\
T(n-1) &= 2T(n-2) + 1\\
&\ \,\vdots\\
T(1) &= 1
\end{aligned}$$
En multipliant la ligne $k$ par $2^k$ et en sommant (étape intermédiaire coupée sur l'image) :
$$T(n) = \sum_{k=0}^{n-1} 2^k = 2^n - 1, \qquad\text{donc } T(n) = \Theta(2^n) : \text{algorithme exponentiel.}$$

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours.

1. **Algorithme D en $O(m \cdot n)$, noté « linéaire »** : $m \cdot n$ n'est pas linéaire (quadratique si $m = n$). Le cours écrit « → linéaire » après chaque algorithme, ce qui est juste pour A, B, C et faux pour D (complément). **À corriger avant un examen.**
2. **`somme_1` et `somme_2`** : le texte dit qu'ils font la même chose. `range(n)` somme $0 + \ldots + (n-1) = \frac{n(n-1)}{2}$, alors que `n * (n + 1) // 2` vaut la somme jusqu'à $n$. Les deux ne coïncident pas (complément). Les complexités $O(n)$ et $O(1)$ restent justes.
3. **Dimension du produit matriciel** : le texte dit que $C$ est de dimension $(m, n)$, alors qu'elle est $(m, p)$ ; « une matrice $C$ de matrice » est à lire « de dimension » (alerte confirmée, complément).
4. **Code des algorithmes** : indentation incertaine sur l'image (`return S`, bloc `else` de l'algorithme D, indentation de `print`). Alertes à vérifier sur l'image, non ouverte.
5. **Hanoï** : l'équation $T(n) = 2T(n-1) + 1$ est introduite pour « $n > 0$ » alors que la base est $T(1) = 1$ ; la fin de la résolution est coupée sur l'image. Le résultat $\sum_0^{n-1} 2^k = 2^n - 1$ est juste.
6. **`recherche_dic` renvoie 0** quand la valeur est trouvée et $-1$ sinon, et non sa position (complément, sans effet sur l'analyse).
7. **Cas moyen de la fonction `f`** : 3,5 suppose les deux branches équiprobables, ce que le texte ne précise pas.
8. **Coquilles recopiées** : « aymptotique » pour « asymptotique », « dichotomqiue », et `i! = indMini` pour `i != indMini` dans le tri de sélection (corrigé dans le bloc de code de cette fiche).
9. **Factorielle, cas $n = 0$** : le cours écrit « $T(n) = 1$ » pour $n = 0$ ; c'est $T(0) = 1$, base de la suite $T(n) = 3n + 1$.
