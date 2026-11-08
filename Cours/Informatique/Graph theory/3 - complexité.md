---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/chp3 - complexité .docx|chp3 - complexité]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/graph theory/chp3 - complexité .docx|chp3 - complexité]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Cours en français. Images non ouvertes : toutes contiennent du texte, du code ou des formules, recopiés ici d'après leur transcription. Voir [[Complexité algorithmique]].

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

Avec ces notations, les trois complexités s'écrivent : [[Complément hors du cours|ⓘ]]
$$T_{\text{pire}}(n) = \max_{d \in D(n)} \text{Coût}_A(d), \qquad T_{\text{meilleur}}(n) = \min_{d \in D(n)} \text{Coût}_A(d), \qquad T_{\text{moyen}}(n) = \sum_{d \in D(n)} P(d) \cdot \text{Coût}_A(d).$$

Le pire cas est le plus utilisé, car c'est une **garantie** : l'algorithme ne fera jamais plus. Le cas moyen dépend d'une hypothèse sur la loi des données (souvent l'équiprobabilité), qui n'est pas toujours réaliste. [[Complément hors du cours|ⓘ]]

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

Détail : pire cas $1 + 3 = 4$ (test puis seconde branche), meilleur cas $1 + 2 = 3$ (test puis première branche) ; le cas moyen $\frac{4 + 3}{2} = 3{,}5$ suppose les deux branches **équiprobables** ($P = \frac{1}{2}$ chacune). Le coût ne dépend pas d'une taille $n$ : la fonction est en $O(1)$. [[Complément hors du cours|ⓘ]]

### Exemple : deux sommes

Le premier programme est en $O(n)$, le second en $O(1)$ ; ils ne renvoient pas tout à fait la même valeur : `somme_1` calcule $0 + 1 + \ldots + (n-1) = \frac{n(n-1)}{2}$ (`range(n)` s'arrête à $n - 1$), `somme_2` calcule $1 + 2 + \ldots + n = \frac{n(n+1)}{2}$. [[Erreurs du cours#^e-3-complexite|✎]]

```python
def somme_1(n):          # somme 0 + 1 + ... + (n-1), par une boucle
    S = 0
    for i in range(n):
        S = S + i
    return S

def somme_2(n):          # somme 1 + 2 + ... + n, par la formule
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

En résumé : $O$ majore, $\Omega$ minore, $\Theta$ encadre, à une constante près et pour $n$ assez grand ; et $f = \Theta(g) \iff f = O(g)$ et $f = \Omega(g)$. Voir [[Comparaison asymptotique]]. [[Complément hors du cours|ⓘ]]

Exemple : $f(n) = 3n^2 + 5n + 2 = \Theta(n^2)$. Pour $n \ge 1$, $3n^2 \le f(n)$ ($k_1 = 3$) ; et $f(n) \le 4n^2 \iff n^2 - 5n - 2 \ge 0$, vrai dès $n \ge 6$ ($k_2 = 4$, $n_0 = 6$). On ne garde que le terme dominant, sans sa constante. [[Complément hors du cours|ⓘ]]

Règles de calcul usuelles : $O(f) + O(g) = O(\max(f, g))$ (deux blocs à la suite : le plus coûteux l'emporte) ; $O(f) \cdot O(g) = O(f \cdot g)$ (une boucle dont le corps coûte $O(g)$, répétée $O(f)$ fois) ; $k \cdot O(f) = O(f)$ pour une constante $k > 0$. [[Complément hors du cours|ⓘ]]

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

Le tableau est rangé par croissance : $1 \ll \log n \ll n \ll n \log n \ll n^2 \ll n^3 \ll 2^n \ll n!$, chaque fonction étant négligeable devant la suivante quand $n \to +\infty$ ([[Croissances comparées]]). [[Complément hors du cours|ⓘ]]

Ordres de grandeur, pour une machine à environ $10^9$ opérations par seconde et $n = 10^6$ : $n \log_2 n \approx 2 \cdot 10^7$ opérations, soit quelques centièmes de seconde ; $n^2 = 10^{12}$, soit environ un quart d'heure ; $n^3$, plus de trente ans. Un algorithme en $2^n$ devient inutilisable bien avant : $2^{60} \approx 1{,}2 \cdot 10^{18}$ opérations demandent déjà plus de trente ans. D'où la frontière entre algorithmes **polynomiaux** ($O(n^k)$), jugés praticables, et **exponentiels**. [[Complément hors du cours|ⓘ]]

Ces « classes » d'ordre de grandeur, qui portent sur un algorithme, ne sont pas les **classes de complexité** de la théorie, qui portent sur un problème : **P** (problèmes résolus par un algorithme polynomial) et **NP** (problèmes dont une solution proposée se vérifie en temps polynomial). Savoir si $P = NP$ est un problème ouvert, l'un des sept « problèmes du millénaire » du Clay Mathematics Institute (2000). Le [[Problème du voyageur de commerce]] et le [[Problème du sac à dos]] sont, dans leur version de décision, des problèmes NP-complets : on ne leur connaît aucun algorithme polynomial. Voir [[Classes P et NP]]. [[Complément hors du cours|ⓘ]]

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

La boucle `while` des algorithmes C et D fait partie du corps de la fonction : elle est indentée sous `def`. [[Erreurs du cours#^e-3-complexite|✎]]

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
**$O(m \cdot n)$** : ce n'est pas linéaire (quadratique si $m = n$). [[Erreurs du cours#^e-3-complexite|✎]]

(Les codes sont écrits `def Algorithm_A :` sans parenthèses dans le cours : du pseudo-code à la syntaxe Python.)

Le raisonnement, qui consiste à compter les tours de boucle : [[Complément hors du cours|ⓘ]]
- **A** : $i$ et $j$ avancent ensemble, et la boucle s'arrête dès que **l'un** dépasse sa borne, donc après $\min(m, n)$ tours. [[Complément hors du cours|ⓘ]]
- **B** : avec `or`, la boucle continue tant que **l'un** reste dans sa borne, donc $\max(m, n)$ tours. [[Complément hors du cours|ⓘ]]
- **C** : $i$ monte d'abord jusqu'à $m + 1$ ($m$ tours), puis seul $j$ avance ($n$ tours) : $m + n$ tours. [[Complément hors du cours|ⓘ]]
- **D** : pour chacune des $n$ valeurs de $j$, $i$ refait tout le parcours de 1 à $m + 1$ avant d'être remis à 1 : environ $(m + 1) \cdot n$ tours. C'est la structure de deux **boucles imbriquées**, d'où le produit. [[Complément hors du cours|ⓘ]]

### Recherche séquentielle d'une valeur dans un tableau

Voir [[Recherche séquentielle]].
- **Pire cas** : $x$ ne figure pas dans le tableau ; $n$ itérations : $T(n) = O(n)$.
- **Meilleur cas** : $x$ est le premier élément : $T(n) = O(1)$.
- **Cas moyen** : données réparties avec la probabilité $\frac{1}{n}$ :
$$T(n) = \sum_{i=1}^{n} \frac{1}{n} \cdot i = \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{n+1}{2}, \quad\text{donc } T(n) = O(n).$$

### Recherche dichotomique dans un tableau trié

Voir [[Recherche dichotomique]]. Si la valeur est trouvée, la fonction renvoie sa position `m` ; sinon $-1$. [[Erreurs du cours#^e-3-complexite|✎]]

```python
def recherche_dic(x, t):
    d = 0
    f = len(t) - 1
    while (d <= f):
        m = (d + f) // 2
        if t[m] == x:
            return m
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

Comme $v_{2^0} = v_1 = 1$, on obtient $v_{2^k} \le k + 1$, c'est-à-dire $v_n \le \log_2 n + 1$. Pour $2^k \le n < 2^{k+1}$, le nombre d'itérations est au plus $v_{2^{k+1}} \le k + 2 \le \log_2 n + 2$ : toujours $O(\log n)$. Concrètement, un tableau trié d'un million d'éléments ($\approx 2^{20}$) demande au plus une vingtaine de comparaisons, contre un million pour la recherche séquentielle. [[Complément hors du cours|ⓘ]]

La recherche dichotomique suppose le tableau **trié** : si on doit d'abord le trier (au mieux en $O(n \log n)$ par comparaisons), elle ne devient rentable que si l'on fait de nombreuses recherches dans le même tableau. [[Complément hors du cours|ⓘ]]

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

Le test s'écrit `if i != indMini:`. [[Erreurs du cours#^e-3-complexite|✎]] On ne compte que les instructions colorées dans le cours : en rouge, celles de la boucle externe (`indMini = i`, le test `i != indMini` et les trois affectations de l'échange, soit 5) ; en vert, celles de la boucle interne (le test et `indMini = j`, soit 2).

**Pire cas** : tableau trié dans l'ordre décroissant.
$$T(n) = 5(n-1) + \sum_{i=1}^{n-1} 2i = 5(n-1) + \frac{2n(n-1)}{2} = 5n - 5 + n^2 - n = n^2 + 4n - 5.$$
Donc $T(n) = O(n^2)$.

Le meilleur cas (tableau déjà trié) ne change pas l'ordre de grandeur : la boucle interne fait toujours ses $n - 1 - i$ comparaisons, soit $\sum_{i=0}^{n-2} (n - 1 - i) = \frac{n(n-1)}{2}$ comparaisons au total ; seuls `indMini = j` et l'échange sont évités. Le tri par sélection est donc en $\Theta(n^2)$ **dans tous les cas**. En revanche, il fait au plus $n - 1$ échanges, ce qui le rend intéressant quand déplacer un élément coûte cher. [[Complément hors du cours|ⓘ]]

### Tri d'insertion non récursif

**Exercice** : écrire une fonction Python de [[Tri par insertion|tri par insertion]] et étudier sa complexité. La note ne donne pas de correction.

Une correction possible : on insère `t[i]` dans la partie gauche `t[0..i-1]`, déjà triée, en décalant vers la droite les éléments plus grands. [[Complément hors du cours|ⓘ]]

```python
def triInsertion(t):
    for i in range(1, len(t)):
        x = t[i]
        j = i - 1
        while j >= 0 and t[j] > x:
            t[j + 1] = t[j]
            j = j - 1
        t[j + 1] = x
```

Complexité, en comptant les comparaisons `t[j] > x` : [[Complément hors du cours|ⓘ]]
- **pire cas** (tableau trié dans l'ordre décroissant) : l'élément d'indice $i$ est comparé à tous ceux de gauche, soit $\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}$ comparaisons : $\Theta(n^2)$ ; [[Complément hors du cours|ⓘ]]
- **meilleur cas** (tableau déjà trié) : une seule comparaison par élément, soit $n - 1$ : $\Theta(n)$ ; [[Complément hors du cours|ⓘ]]
- **cas moyen** (toutes les permutations équiprobables) : environ $\frac{n^2}{4}$ comparaisons, donc $\Theta(n^2)$. [[Complément hors du cours|ⓘ]]

Contrairement au tri par sélection, le tri par insertion profite d'un tableau presque trié. [[Complément hors du cours|ⓘ]]

### Produit matriciel

On considère deux matrices $A$ et $B$ de dimensions $(m, n)$ et $(n, p)$. Le [[Produit matriciel|produit]] de $A$ par $B$ est une matrice $C$ de dimension $(m, p)$ définie par [[Erreurs du cours#^e-3-complexite|✎]]
$$C_{i,j} = \sum_{k=1}^{n} A_{i,k} \cdot B_{k,j}.$$

La note s'arrête là, sans calcul de complexité.

L'algorithme naïf fait trois boucles imbriquées ($i$ de 1 à $m$, $j$ de 1 à $p$, $k$ de 1 à $n$) : chacun des $m \cdot p$ coefficients demande $n$ multiplications et $n - 1$ additions. Le coût est donc $\Theta(m \cdot n \cdot p)$, soit $\Theta(n^3)$ pour deux matrices carrées $n \times n$ (complexité **cubique**). [[Complément hors du cours|ⓘ]]

Le code correspondant : [[Complément hors du cours|ⓘ]]

```python
def produit(A, B):
    m, n, p = len(A), len(B), len(B[0])
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C
```

On sait faire mieux : l'algorithme de Strassen (1969), de type [[Diviser pour régner|diviser pour régner]], multiplie deux matrices carrées en $O(n^{\log_2 7}) \approx O(n^{2{,}81})$ en remplaçant 8 produits de sous-matrices par 7. [[Complément hors du cours|ⓘ]]

## Complexité des algorithmes récursifs

Un algorithme récursif décompose un problème en **sous-problèmes de même nature**, puis recompose leurs solutions. La **complexité d'un algorithme récursif est une suite définie par récurrence** (voir [[Calcul de complexité et théorème de résolution]] et [[Récursivité]]).

Trois méthodes classiques pour résoudre une telle récurrence : les **substitutions successives** (dérouler la récurrence jusqu'au cas de base, comme pour Hanoï ci-dessous), l'**arbre des appels** (sommer le coût de chaque niveau d'appels), et, pour les récurrences de la forme « diviser pour régner », le **théorème maître** (*master theorem*). [[Complément hors du cours|ⓘ]]

**Théorème maître (forme simplifiée).** Si $T(n) = a\,T(n/b) + \Theta(n^d)$ avec $a \ge 1$, $b > 1$ et $d \ge 0$ : [[Complément hors du cours|ⓘ]]
- si $d > \log_b a$, alors $T(n) = \Theta(n^d)$ ; [[Complément hors du cours|ⓘ]]
- si $d = \log_b a$, alors $T(n) = \Theta(n^d \log n)$ ; [[Complément hors du cours|ⓘ]]
- si $d < \log_b a$, alors $T(n) = \Theta(n^{\log_b a})$. [[Complément hors du cours|ⓘ]]

Exemples : la recherche dichotomique vérifie $T(n) = T(n/2) + \Theta(1)$ ($a = 1$, $b = 2$, $d = 0 = \log_2 1$), d'où $\Theta(\log n)$, ce qui retrouve le résultat ci-dessus ; le tri fusion vérifie $T(n) = 2T(n/2) + \Theta(n)$ ($d = 1 = \log_2 2$), d'où $\Theta(n \log n)$. Le théorème ne s'applique pas à $T(n) = T(n-1) + c$ ni à $T(n) = 2T(n-1) + 1$, où la taille diminue d'une unité et non d'un facteur : c'est le cas de la factorielle et de Hanoï, traités par substitution. [[Complément hors du cours|ⓘ]]

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

Le calcul : en déroulant, $T(n) = T(n-1) + 3 = T(n-2) + 2 \cdot 3 = \ldots = T(0) + 3n = 3n + 1$. [[Complément hors du cours|ⓘ]]

La récursivité a aussi un coût en **mémoire** : avant de calculer, `factorielleRecursive(n)` empile $n + 1$ appels sur la [[Pile d'exécution|pile d'exécution]], d'où une complexité spatiale en $\Theta(n)$, alors qu'une version itérative (une boucle et une variable) se contente de $O(1)$. En Python, la profondeur de récursion est limitée par défaut à 1 000 appels environ (`sys.getrecursionlimit()`), au-delà de quoi l'appel lève une `RecursionError`. [[Complément hors du cours|ⓘ]]

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
- Si $n > 1$ : un test et deux appels récursifs sur $n - 1$ : [[Erreurs du cours#^e-3-complexite|✎]]
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

L'étape intermédiaire : la ligne $k$ (pour $k = 0, \ldots, n-2$) s'écrit $T(n-k) = 2T(n-k-1) + 1$ ; multipliée par $2^k$, elle devient $2^k T(n-k) = 2^{k+1} T(n-k-1) + 2^k$. En sommant ces $n - 1$ lignes, les termes en $T$ se simplifient deux à deux ([[Somme télescopique|somme télescopique]]) et il reste $T(n) = 2^{n-1} T(1) + \sum_{k=0}^{n-2} 2^k = 2^{n-1} + \sum_{k=0}^{n-2} 2^k = \sum_{k=0}^{n-1} 2^k$, qui vaut $2^n - 1$ par la somme d'une [[Suite géométrique|suite géométrique]] de raison 2. [[Complément hors du cours|ⓘ]]

Le nombre de déplacements affichés vérifie la même récurrence, donc vaut aussi $2^n - 1$ ; on montre que c'est le **minimum** possible : le plus grand disque doit bouger au moins une fois, et il faut pour cela avoir d'abord déplacé les $n - 1$ autres, puis les replacer. Avec les 64 disques de la légende du jeu, il faudrait $2^{64} - 1 \approx 1{,}8 \cdot 10^{19}$ déplacements, soit près de 600 milliards d'années à un déplacement par seconde. [[Complément hors du cours|ⓘ]]
