---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/Cours/Chp1 - récursivité et complexité.docx|Chp1 - récursivité et complexité]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[Raw/Year 2/Algo/Cours/Chp1 - récursivité et complexité.docx|Chp1 - récursivité et complexité]], dans [[Algo (matière)]]. En cas d'écart, le cours et ses images font foi. Les exemples sont en [[Langage Python|Python]].

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

## 2. Pile de récursion

Lors de l'exécution d'un algorithme récursif, les appels successifs sont stockés dans une pile : la **pile de récursion** (voir [[Pile d'exécution]] et [[Pile et file]]).

- La **pile d'exécution** est plus générale et gère tous les appels de fonctions.
- La **pile de récursion** en est un cas particulier, qui ne s'applique qu'aux appels récursifs, mais utilise la même structure.

C'est un emplacement mémoire qui stocke les paramètres, les variables locales et les adresses de retour des fonctions en cours d'exécution.

- En Python, la pile de récursion est limitée à **environ 1000 appels**.
- Chaque appel de fonction génère son **bloc**, qui contient :
  - les paramètres reçus lors de l'appel ;
  - l'adresse de réponse (normalement le bloc du dessous) ;
  - les variables locales de cet appel.

![[Chp1 - récursivité et complexité - image6.png]]
*Figure : pile des appels de `f` (somme) : empilement de `f(5) → 5 + f(4)` jusqu'à `f(0) → 0`, puis dépilement avec les valeurs renvoyées 0, 1, 3, 6, 10, 15.*

![[Chp1 - récursivité et complexité - image12.png]]
*Figure : pile de récursion pour la factorielle de 5 : la pile se remplit au fil des appels, puis se vide en renvoyant 1, 1, 2, 6, 24.*

- Quand on arrive au cas de base, le bloc du haut donne sa réponse au bloc du dessous et disparaît.
- À la fin, il ne reste en mémoire que le bloc de `fact(5)`, qui finit son exécution et disparaît.
- C'est pour cela que les espaces de noms disparaissent.

## 3. Calcul de complexité

**Définition.** La [[Complexité algorithmique|complexité]] d'un algorithme $A$ est le calcul de la quantité de ressources (temps $t$) nécessaire pour résoudre un problème $P$ au moyen de l'exécution de $A$, en fonction de la taille $n$ de $P$ et indépendamment de la performance de la machine.

Trois types de complexité :

- **au meilleur** : le plus petit nombre d'opérations qu'exécutera l'algorithme sur un jeu de données de taille $n$ ;
- **au pire** : le plus grand nombre d'opérations sur un jeu de données de taille $n$ (on veut être sûr que l'algorithme ne prendra jamais plus de temps que l'estimation) ;
- **en moyenne** : la moyenne des complexités sur les jeux de données de taille $n$.

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

## 4. Complexité d'une fonction récursive

Elle se décompose en deux termes :

1. la complexité due aux **appels récursifs** ;
2. la complexité due aux calculs qui **séparent les données** pour réaliser les appels, ou **reconstruisent le résultat** après les appels.

Il faut déterminer le nombre d'appels récursifs et la complexité de chaque appel. On peut utiliser la **méthode de substitution** : remplacer chaque appel récursif par une expression mathématique pour obtenir la complexité totale.

### Exemple de substitution

$$T(n) = \begin{cases} c & \text{si } n = 0 \\ T(n-1) + b & \text{sinon} \end{cases}$$

$$\begin{aligned}
T(n) &= b + T(n-1) \\
&= b + [b + T(n-2)] = 2b + T(n-2) \\
&= ib + T(n-i) \\
&= ib + [b + T(n-i+1)] \\
&= (n-1)b + T(n-n+1) = nb - b + T(1) = nb - b + c
\end{aligned}$$

$T(n) = nb - b + c$, donc $O(n)$ (calcul recopié tel quel, voir point à vérifier 1).

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

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Toutes les images ont été lues par leur transcription ; aucune n'a été ouverte.

1. **Substitution de $T(n) = T(n-1) + b$** (complément) : la base est $T(0) = c$, mais la dernière ligne s'arrête sur $T(1)$ et écrit $nb - b + c$. Avec la base $T(0)$, on obtient $nb + c$. Le résultat $O(n)$ est le même. La ligne « $ib + [b + T(n-i+1)]$ » semble aussi fautive (on attendrait $T(n-i-1)$).
2. **Exemple annoté de la factorielle** : la transcription signale que les annotations sont décalées par rapport au code. Alerte confirmée par le texte, pas par l'image. La conclusion écrite à côté (« La complexité est $O(n)$ ») est juste.
3. **Fausse alerte** : le « 1 » de la factorielle lu comme un « I » dans les transcriptions est bien le chiffre 1, le calcul de la phase de montée le confirme.
4. **Pied de page « TIME UN — 4 2 »** du graphique des complexités : bruit de mise en page, sans contenu.
5. **Master theorem** : le cours le donne sans démonstration, pour $f(n) = c\,n^k$ seulement. Le cours le nomme aussi « Master Theorem » dans l'analyse de la dichotomie.
6. **Petits chiffres de la pile de la factorielle de 5** (image12) : peu lisibles selon la transcription, non vérifiés sur l'image.
