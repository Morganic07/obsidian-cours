---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/Cours/Chp1 - récursivité et complexité.docx|Chp1 - récursivité et complexité]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 2/Algo/Cours/Chp1 - récursivité et complexité.docx|Chp1 - récursivité et complexité]], dans [[Cours/Informatique/Algo/_index|Algo]]. Les exemples sont en [[Langage Python|Python]].

## Idée générale

Une fonction récursive s'appelle elle-même, et l'on mesure le coût d'un algorithme par son ordre de grandeur plutôt que par un temps exact. Le chapitre relie les deux : le coût d'une fonction récursive se met en équation, puis se résout.

## 1. Récursivité

**Définition.** Une fonction est [[Récursivité|récursive]] si et seulement si elle est définie directement ou indirectement en fonction d'elle-même.

- **Récursivité directe** : le corps de `A(...)` contient un appel à `A(...)`.
- **Récursivité indirecte** : `B` appelle `C`, `C` appelle `D`, et `D` rappelle `B`.

![[Chp1 - récursivité et complexité - image2.png]]
*Figure : récursivité directe (A s'appelle lui-même) et indirecte (cycle B → C → D → B).*

### Les deux phases

| Phase | Déroulement |
|---|---|
| Descente | Chaque appel récursif fait un appel récursif jusqu'à atteindre une condition d'arrêt |
| Montée | Quand la condition d'arrêt est atteinte, on remonte chaque appel |

### Exemple : la factorielle

$$n! = \begin{cases} 1 & \text{si } n = 0 \\ n \times (n-1)! & \text{sinon} \end{cases}$$

Voir [[Factorielle]].

Version itérative (itérative car elle utilise une [[Boucle (programmation)|boucle]] `for` ou `while`) :

```python
def fact(n):
    p = 1
    for i in range(2, n+1):
        p = p * i
    return p

print(fact(6))
```

Version récursive :

```python
def fact(n):
    if n == 0:          # condition d'arrêt
        return 1
    else:               # appel récursif
        return n * fact(n-1)
```

On code une fonction récursive en deux parties :

- une **condition d'arrêt** pour stopper les appels récursifs (avec un `if`) ;
- les **appels récursifs**.

La fonction récursive doit avoir des `return` pour pouvoir faire appel à elle-même.

La condition d'arrêt ne suffit pas : il faut aussi que chaque appel s'en **rapproche**, en général parce que le paramètre décroît strictement (`n` → `n-1`) vers le cas de base. C'est ce qui garantit la [[Terminaison d'un algorithme|terminaison]]. Appeler `fact(-1)` ne termine jamais : $n$ décroît sans jamais valoir 0, et les appels s'accumulent jusqu'à saturer la pile (voir la section 2). [[Complément hors du cours|ⓘ]]

![[Chp1 - récursivité et complexité - image15.png]]
*Figure : `fact(4)` ; phase de descente jusqu'à la condition terminale `fact(0) ← 1`, puis phase de remontée : `fact(1) ← 1`, `fact(2) ← 2`, `fact(3) ← 6`, `fact(4) ← 24`.*

### Exemple : somme des premiers entiers

Pour calculer la somme des 100 premiers entiers (voir [[Somme des premiers entiers]]) :

```python
# itératif
def somme(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total

# récursif
def somme(n):
    if n > 0:
        return n + somme(n-1)
    return 0
```

### Récursivité multiple : la suite de Fibonacci

Une fonction peut faire **plusieurs** appels récursifs dans son corps. Exemple classique, la [[Suite de Fibonacci]] : $F_0 = 0$, $F_1 = 1$, $F_n = F_{n-1} + F_{n-2}$. [[Complément hors du cours|ⓘ]]

```python
def fibo(n):
    if n < 2:           # condition d'arrêt : F(0) = 0, F(1) = 1
        return n
    return fibo(n-1) + fibo(n-2)
```

Cette version, fidèle à la définition, est très lente : `fibo(n-2)` est recalculé dans `fibo(n-1)`, et ainsi de suite, si bien que le nombre d'appels croît comme $\varphi^n$ avec $\varphi = \frac{1+\sqrt5}{2} \approx 1{,}618$ (complexité exponentielle). En mémorisant les valeurs déjà calculées (**mémoïsation**, idée de la [[Programmation dynamique|programmation dynamique]]) ou en écrivant une boucle sur deux variables, on revient à $O(n)$. Une récursion naturelle n'est donc pas toujours efficace. [[Complément hors du cours|ⓘ]]

## 2. Pile de récursion

Lors de l'exécution d'un algorithme récursif, les appels successifs sont stockés dans une pile : la **pile de récursion** (voir [[Pile d'exécution]] et [[Pile et file]]).

- La **pile d'exécution** est plus générale et gère tous les appels de fonctions.
- La **pile de récursion** en est un cas particulier, qui ne s'applique qu'aux appels récursifs, mais utilise la même structure.

C'est un emplacement mémoire qui stocke les paramètres, les variables locales et les adresses de retour des fonctions en cours d'exécution.

- En Python, la pile de récursion est limitée à **environ 1000 appels**.
- Au-delà, Python lève l'exception `RecursionError: maximum recursion depth exceeded`. La limite se lit avec `sys.getrecursionlimit()` et se change avec `sys.setrecursionlimit(n)` (module `sys`), mais la relever trop haut peut faire planter l'interpréteur. Python n'optimise pas la [[Récursivité terminale|récursivité terminale]] : même écrite avec un accumulateur, une fonction récursive consomme un bloc par appel. Pour de grandes valeurs, la version itérative reste préférable. [[Complément hors du cours|ⓘ]]
- Chaque appel de fonction génère son **bloc**, qui contient :
  - les paramètres reçus lors de l'appel ;
  - l'adresse de réponse (normalement le bloc du dessous) ;
  - les variables locales de cet appel.

![[Chp1 - récursivité et complexité - image6.png]]
*Figure : pile des appels de `f` (somme) : empilement de `f(5) → 5 + f(4)` jusqu'à `f(0) → 0`, puis dépilement avec les valeurs renvoyées 0, 1, 3, 6, 10, 15.*

![[Chp1 - récursivité et complexité - image12.png]]
*Figure : pile de récursion pour factorielle de 4 (`fact(4)`) : la pile se remplit au fil des appels (« 4× », « 3× », « 2× », « 1× »), puis se vide en renvoyant 1, 1, 2, 6, 24.* [[Erreurs du cours#^e-1-recursivite-et-complexite|✎]]

- Quand on arrive au cas de base, le bloc du haut donne sa réponse au bloc du dessous et disparaît.
- À la fin, il ne reste en mémoire que le bloc de `fact(5)`, qui finit son exécution et disparaît.
- C'est pour cela que les espaces de noms disparaissent.

## 3. Calcul de complexité

**Définition.** La [[Complexité algorithmique|complexité]] d'un algorithme $A$ est le calcul de la quantité de ressources (temps $t$) nécessaire pour résoudre un problème $P$ au moyen de l'exécution de $A$, en fonction de la taille $n$ de $P$ et indépendamment de la performance de la machine.

Trois types de complexité :

- **au meilleur** : le plus petit nombre d'opérations qu'exécutera l'algorithme sur un jeu de données de taille $n$ ;
- **au pire** : le plus grand nombre d'opérations sur un jeu de données de taille $n$ (on veut être sûr que l'algorithme ne prendra jamais plus de temps que l'estimation) ;
- **en moyenne** : la moyenne des complexités sur les jeux de données de taille $n$.

Exemple, pour la recherche séquentielle d'une valeur dans un tableau de $n$ cases : au meilleur, elle est dans la première case (1 comparaison) ; au pire, elle est absente ou dans la dernière ($n$ comparaisons) ; en moyenne, si elle est présente et que chaque position est également probable, il faut $\frac{n+1}{2}$ comparaisons, soit encore $O(n)$. Voir [[Recherche séquentielle]]. [[Complément hors du cours|ⓘ]]

On mesure de la même façon la **complexité spatiale** : la mémoire utilisée en fonction de $n$. La factorielle itérative n'utilise que deux variables, $O(1)$ ; la version récursive empile $n+1$ blocs avant de remonter (section 2), soit $O(n)$. À complexité en temps égale, l'itératif économise donc souvent la mémoire. [[Complément hors du cours|ⓘ]]

### Règles de calcul

- Chaque instruction basique consomme une unité de temps (affectation, comparaison…).
- Chaque itération d'une boucle rajoute le nombre d'unités de temps consommées dans le corps de la boucle.
- Chaque appel de fonction rajoute le nombre d'unités de temps consommées dans cette fonction.
- Pour le nombre total d'opérations, on additionne le tout.

On ne calcule généralement pas la complexité exacte mais son **ordre de grandeur**, une valeur asymptotique : pour $n^2 + 2n - 5$ opérations, on retient $O(n^2)$.

### Règles de la notation $O$

Voir [[Calcul de complexité et théorème de résolution]].

- On oublie les constantes multiplicatives (elles valent 1).
- On annule les constantes additives.
- On ne retient que les termes dominants.

$$O(c) = O(1) \qquad O(cT) = c\,O(T) = O(T)$$
$$O(T_1) + O(T_2) = O(T_1 + T_2) = \max(O(T_1), O(T_2)) \qquad O(T_1)\,O(T_2) = O(T_1 T_2)$$

Les instructions de base prennent un temps constant, noté $O(1)$.

Définition précise : $T(n) = O(g(n))$ s'il existe une constante $c > 0$ et un rang $n_0$ tels que $T(n) \le c\,g(n)$ pour tout $n \ge n_0$. $O$ est donc une **borne supérieure** à une constante près, à partir d'un certain rang ; c'est pourquoi les constantes et les termes non dominants disparaissent. Pour $n^2 + 2n - 5$ : dès $n \ge 1$, $n^2 + 2n - 5 \le 3n^2$, donc $O(n^2)$ avec $c = 3$, $n_0 = 1$. Voir [[Comparaison asymptotique]]. [[Complément hors du cours|ⓘ]]

Deux notations voisines, que le cours emploie plus bas sans les définir ([[Complexité algorithmique]]) : [[Complément hors du cours|ⓘ]]
- $T(n) = \Omega(g(n))$ : **borne inférieure**, il existe $c > 0$ et $n_0$ tels que $T(n) \ge c\,g(n)$ pour $n \ge n_0$ ;
- $T(n) = \Theta(g(n))$ : **ordre de grandeur exact**, à la fois $O(g(n))$ et $\Omega(g(n))$. Par exemple, $\Theta(1)$ signifie « borné par des constantes », ni plus ni moins.

### `while` et `if`

```text
# en supposant qu'on a m itérations
while <condition>:        O(g(n))
    # instructions        O(f(n))
                          } = O(m * (g(n) + f(n)))

if <condition>:           O(g(n))
    # instructions (1)    O(f1(n))
else:
    # instructions (2)    O(f2(n))
                          = O(g(n) + f1(n) + f2(n))
```

### Classes de complexité

![[Chp1 - récursivité et complexité - image14.png]]
*Figure : $T(n)$ en fonction de $n$, de la croissance la plus rapide à la plus lente : exponentielle $a^n$, $n^3$, quadratique $n^2$, $n\log n$, $n$, $\log n$.*

On parle de complexité (voir [[Classe de complexité]]) :

| Nom | $C(n)$ |
|---|---|
| En temps constant | $O(1)$ |
| Logarithmique | $O(\ln n)$ |
| Linéaire | $O(n)$ |
| Quadratique | $O(n^2)$ |
| Polynomiale de degré $p$ | $O(n^p)$ |
| Exponentielle | $O(a^n)$ pour un certain $a$ |

Deux classes manquent au tableau : la **quasi-linéaire** $O(n \log n)$, pourtant sur la figure (les bons algorithmes de tri, comme le [[Tri fusion|tri fusion]]), et la **factorielle** $O(n!)$, plus rapide encore que l'exponentielle (essayer toutes les permutations, comme dans la recherche exhaustive du [[Problème du voyageur de commerce]]). [[Complément hors du cours|ⓘ]]

Dans une complexité logarithmique, la base ne compte pas : $\log_b n = \dfrac{\ln n}{\ln b}$, donc $\log_2 n$ et $\ln n$ ne diffèrent que d'une constante multiplicative et $O(\ln n) = O(\log_2 n)$. Le tableau écrit $\ln$, la dichotomie (section 5) donne $\log_2$ : c'est la même classe. [[Complément hors du cours|ⓘ]]

Ordres de grandeur pour $n = 1000$ : $\log_2 n \approx 10$, $n \log_2 n \approx 10^4$, $n^2 = 10^6$, $n^3 = 10^9$, et $2^n \approx 10^{301}$. Une machine qui fait un milliard d'opérations par seconde traite $n^3$ en une seconde, mais $2^n$ jamais : un algorithme exponentiel est inutilisable dès que $n$ dépasse quelques dizaines. [[Complément hors du cours|ⓘ]]

### Exemple : factorielle itérative

```python
def factorielle(n):
    fact = 1          # affectation : 1
    i = 2             # affectation : 1
    while i <= n:     # itérations : (n − 1), comparaison : 1
        fact = fact * i   # multiplication + affectation : 2
        i = i + 1         # addition + affectation : 2
    return fact
```

Annotations replacées d'après leur sens (elles sont décalées dans l'image). Conclusion du cours : **la complexité est $O(n)$**.

Le décompte complet : 2 affectations initiales, puis $n-1$ tours de boucle coûtant chacun 1 comparaison et 4 opérations, plus la dernière comparaison qui fait sortir de la boucle : $T(n) = 2 + 5(n-1) + 1 = 5n - 2$ (sans compter le `return`). Les règles de la notation $O$ effacent le 5 et le $-2$ : $O(n)$. [[Complément hors du cours|ⓘ]]

## 4. Complexité d'une fonction récursive

Elle se décompose en deux termes :

1. la complexité due aux **appels récursifs** ;
2. la complexité due aux calculs qui **séparent les données** pour réaliser les appels, ou **reconstruisent le résultat** après les appels.

Il faut déterminer le nombre d'appels récursifs et la complexité de chaque appel. On peut utiliser la **méthode de substitution** : remplacer chaque appel récursif par une expression mathématique pour obtenir la complexité totale.

### Exemple de substitution

Cette récurrence est celle de la factorielle récursive : $c$ est le coût du cas `n == 0` (un test et un `return`), $b$ celui d'un appel qui n'est pas terminal (le test, la soustraction `n-1`, la multiplication, le `return`), et $T(n-1)$ le coût de l'appel `fact(n-1)`. [[Complément hors du cours|ⓘ]]

$$T(n) = \begin{cases} c & \text{si } n = 0 \\ T(n-1) + b & \text{sinon} \end{cases}$$

$$\begin{aligned}
T(n) &= b + T(n-1) \\
&= b + [b + T(n-2)] = 2b + T(n-2) \\
&= ib + T(n-i) \\
&= ib + [b + T(n-i-1)] = (i+1)b + T(n-i-1) \\
&= nb + T(n-n) = nb + T(0) = nb + c
\end{aligned}$$

$T(n) = nb + c$, donc $O(n)$. [[Erreurs du cours#^e-1-recursivite-et-complexite|✎]]

### Diviser pour régner

![[Chp1 - récursivité et complexité - image3.png]]
*Figure : [[Diviser pour régner]] : diviser le problème global en $k$ sous-problèmes de taille moindre, régner en résolvant chacun par la même décomposition récursive jusqu'à des sous-problèmes triviaux, combiner les sous-solutions en une solution globale.*

### Forme générale et théorème de résolution

De manière générale :

$$T(n) = a\,T(n/b) + f(n)$$

- $a$ : on divise le problème en $a$ sous-problèmes, chacun de taille $1/b$ de la taille initiale ;
- $b$ : le ratio de division du problème ;
- $f(n)$ : le coût des calculs pour séparer les problèmes et reconstruire le résultat.

**Théorème de résolution de la récurrence** (*Master Theorem*). Avec $T(n) = a\,T(n/b) + f(n)$ et $f(n) = c\,n^k$ :

$$O(T(n)) = \begin{cases} O(n^{\log_b a}) & \text{si } a > b^k \\ O(n^k \log_b n) & \text{si } a = b^k \\ O(f(n)) = O(n^k) & \text{si } a < b^k \end{cases}$$

Le théorème suppose $a \ge 1$, $b > 1$ et $k \ge 0$. Son sens : l'arbre des appels a $\log_b n$ niveaux et $n^{\log_b a}$ feuilles ; on compare le travail des feuilles ($n^{\log_b a}$) au travail de séparation et de reconstruction à la racine ($n^k$). Si les feuilles dominent ($a > b^k$), elles imposent le coût ; si c'est la racine ($a < b^k$), c'est $f(n)$ ; à égalité, chaque niveau coûte environ $n^k$, d'où le facteur $\log_b n$. [[Complément hors du cours|ⓘ]]

Exemples : [[Complément hors du cours|ⓘ]]
- le [[Tri fusion|tri fusion]] coupe le tableau en deux moitiés triées récursivement, puis les fusionne en temps linéaire : $T(n) = 2T(n/2) + cn$, donc $a = 2$, $b = 2$, $k = 1$, $a = b^k$ et $T(n) = O(n \log n)$ ;
- $T(n) = 4T(n/2) + cn$ : $a = 4 > b^k = 2$, donc $O(n^{\log_2 4}) = O(n^2)$ ;
- $T(n) = 2T(n/2) + cn^2$ : $a = 2 < b^k = 4$, donc $O(n^2)$.

La récurrence $T(n) = T(n-1) + b$ de la factorielle n'entre pas dans ce cadre : le problème n'est pas divisé par $b > 1$ mais réduit de 1. Elle se résout par substitution, comme plus haut. [[Complément hors du cours|ⓘ]]

## 5. Recherche dichotomique

[[Recherche dichotomique|Approche par dichotomie]], sur un tableau trié :

1. On détermine l'élément $m$ au milieu du tableau.
2. Si c'est la valeur recherchée, on s'arrête avec un succès.
3. Sinon :
   - (a) si $m$ est plus grand que la valeur recherchée, comme le tableau est trié, on continue dans la première moitié ;
   - (b) sinon, on cherche dans la moitié droite.
4. On répète jusqu'à trouver la valeur, ou réduire l'intervalle à un intervalle vide : la valeur n'est alors pas présente.

### Version itérative

```python
def recherche_dichotomique(tab, val):
    gauche = 0
    droite = len(tab) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if tab[milieu] == val:
            # on a trouvé val dans le tableau, à la position milieu
            return milieu
        elif tab[milieu] > val:
            # on cherche entre gauche et milieu - 1
            droite = milieu - 1
        else:  # on a tab[milieu] < val
            # on cherche entre milieu + 1 et droite
            gauche = milieu + 1
    # on est sorti de la boucle sans trouver val
    return -1
```

### Version récursive

```python
def rechercheDichoRec(tab, debut, fin, valeur):
    if fin < debut: return -1
    else:
        ind_milieu = (debut + fin)//2
        if tab[ind_milieu] == valeur: return ind_milieu
        if valeur < tab[ind_milieu]:
            return rechercheDichoRec(tab, debut, ind_milieu-1, valeur)
        else:
            return rechercheDichoRec(tab, ind_milieu+1, fin, valeur)

def rechercheDicho(tab, valeur):
    return rechercheDichoRec(tab, 0, len(tab)-1, valeur)
```

### Complexité de la version récursive

- Le coût de la séparation des données est constant : calculer `ind_milieu`.
- Le résultat est renvoyé immédiatement : le coût de reconstruction est nul. Le coût total de ces opérations est $\Theta(1)$.
- Le problème est divisé en 1 problème de taille deux fois plus petite : dans la notation du *Master Theorem*, $a = 1$, $b = 2$ et $f(n) = \Theta(1)$.
- D'où $T(n) = T(n/2) + \Theta(1)$, avec $\log_b a = \log_2 1 = 0$ et $f(n) = \Theta(1) = \Theta(n^0)$ : on est dans le cas $a = b^k$ ($k = 0$).

$$\text{Complexité} = O(n^0 \log_2 n) = O(\log_2 n)$$

On le retrouve sans le théorème : chaque étape divise l'intervalle par deux, et après $p$ étapes il reste environ $n/2^p$ cases ; l'intervalle devient vide dès que $2^p > n$, donc après au plus $\lfloor \log_2 n \rfloor + 1$ comparaisons avec le milieu. Pour un tableau d'un million d'éléments, cela fait au plus 20 comparaisons, contre un million pour la [[Recherche séquentielle|recherche séquentielle]] dans le pire cas. Le prix à payer : le tableau doit être trié. [[Complément hors du cours|ⓘ]]

La version itérative a la même complexité en temps, $O(\log n)$, mais n'utilise que trois variables, soit $O(1)$ en mémoire ; la version récursive empile environ $\log_2 n$ blocs, $O(\log n)$ en mémoire. [[Complément hors du cours|ⓘ]]
