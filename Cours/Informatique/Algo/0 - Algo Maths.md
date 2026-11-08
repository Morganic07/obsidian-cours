---
type: source
tags:
  - year1
sources:
  - "[[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]]"
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]] (séance du 21/09/23), dans [[Cours/Informatique/Algo/_index|Algo]]. Pas d'image dans cette note : les dessins n'en restent que par leur texte.

## Idée générale

Premier cours d'algorithmique : notions de base, puis des problèmes qui introduisent la [[Récurrence]] et la [[Récursivité]].

## Repères et notions de base

- **Ada Lovelace** (1815-1852) a écrit le premier programme.
- Ce programme figure dans ses notes de 1843 sur la **machine analytique** de Charles Babbage, une calculatrice mécanique programmable par cartes perforées, jamais construite : il calcule les nombres de Bernoulli. Elle y pressent aussi qu'une telle machine pourrait manipuler autre chose que des nombres (symboles, musique). [[Complément hors du cours|ⓘ]]
- **[[Algorithme]]** : production automatique d'un résultat à partir d'une entrée. Existe depuis 4000 ans ; le mot vient du nom francisé d'Al-Khwarizmi (vers 780-850). [[Erreurs du cours#^e-0-algo-maths|✎]]
- Al-Khwarizmi est un mathématicien persan qui travaillait à Bagdad, à la Maison de la sagesse, au IXe siècle (*Encyclopædia Britannica*) ; le mot « algèbre » vient aussi de son traité (*al-jabr*). Les algorithmes eux-mêmes sont bien plus anciens : les Babyloniens avaient des procédés de calcul (racines carrées, vers −1800), et l'[[Algorithme d'Euclide]] pour le PGCD date d'environ −300. [[Complément hors du cours|ⓘ]]
- Pour mériter le nom d'algorithme, un procédé doit être **fini** (il s'arrête, voir [[Terminaison d'un algorithme]]), **non ambigu** (chaque étape est définie sans interprétation) et **correct** (il donne le bon résultat pour toute entrée, voir [[Correction d'un algorithme]]). [[Complément hors du cours|ⓘ]]
- **Machine** : fait des calculs et produit un résultat. Existe depuis 100 ans.
- Repères : en 1936, Alan Turing définit la [[Machine de Turing]], modèle mathématique de tout calcul mécanique ; les premiers ordinateurs électroniques apparaissent dans les années 1940 (ENIAC, 1945, aux États-Unis) ; l'architecture de von Neumann (1945) range programme et données dans la même mémoire, principe encore suivi aujourd'hui. [[Complément hors du cours|ⓘ]]
- **[[Bit]]** = *Binary Digit*, chiffre binaire.
- Un bit vaut 0 ou 1 ; avec $n$ bits on code $2^n$ valeurs différentes (de $0$ à $2^n - 1$ pour un entier positif), et un **octet** compte 8 bits, soit 256 valeurs. Les nombres s'y écrivent en base 2 : voir [[Numération binaire]]. [[Complément hors du cours|ⓘ]]
- Dans un ordinateur, l'élément important est le **[[Transistor]]**, qui fonctionne grâce à la mécanique quantique.
- Le transistor, inventé en 1947 aux laboratoires Bell, est un interrupteur commandé électriquement : selon la tension sur sa commande, le courant passe (1) ou non (0). En les combinant, on fabrique des portes logiques (ET, OU, NON), puis des additionneurs et des mémoires. Il est fait d'un **semi-conducteur** (silicium) dont le comportement électrique s'explique par la physique quantique (théorie des bandes d'énergie) ; un processeur actuel en compte plusieurs milliards. [[Complément hors du cours|ⓘ]]

## Interprétation géométrique des nombres premiers (les billes)

Un [[Nombre premier]] se reconnaît en rangeant des billes :

- si l'on peut former un rectangle avec $X$ billes, $X$ n'est pas premier ;
- si la seule manière de les placer est une ligne, $X$ est premier.

Exemples : 15 billes forment un rectangle $3 \times 5$ ; 7 billes ne forment qu'une ligne.

Définition exacte : un entier $p \ge 2$ est premier s'il a exactement deux diviseurs positifs, 1 et lui-même. Le « rectangle » doit avoir deux côtés d'au moins 2 billes, sinon toute ligne en serait un ; et **1 n'est pas premier** (il n'a qu'un diviseur), bien qu'une bille seule forme une ligne. Premiers nombres premiers : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29. [[Complément hors du cours|ⓘ]]

Les billes donnent aussi le test pratique : dans un rectangle $a \times b$ avec $a \le b$, on a $a \le \sqrt{X}$. Pour savoir si $X$ est premier, il suffit donc d'essayer les diviseurs de 2 à $\lfloor\sqrt{X}\rfloor$. Pour trouver tous les premiers jusqu'à $N$, le **crible d'Ératosthène** barre successivement les multiples de 2, 3, 5, … : les nombres restants sont premiers. [[Complément hors du cours|ⓘ]]

Deux résultats classiques : il existe une infinité de nombres premiers (démonstration d'Euclide : si $p_1, \dots, p_k$ étaient tous les premiers, $p_1 \cdots p_k + 1$ n'aurait aucun d'eux pour diviseur) ; et tout entier $\ge 2$ s'écrit de façon unique, à l'ordre près, comme produit de nombres premiers (théorème fondamental de l'arithmétique, par exemple $60 = 2^2 \times 3 \times 5$). La difficulté à factoriser de très grands nombres est à la base du chiffrement RSA. [[Complément hors du cours|ⓘ]]

## Somme des $n$ premiers entiers

[[Somme des premiers entiers]], par un dessin : deux escaliers de $1 + 2 + \dots + n$ s'emboîtent en un rectangle $n \times (n+1)$. Texte du dessin : « n+1 ; n ; 2S = n(n+1) ; S = n(n+1)/2 ». D'où [[Erreurs du cours#^e-0-algo-maths|✎]]

$$2S = n(n+1) \quad\Longrightarrow\quad S = \frac{n(n+1)}{2}.$$

La même idée s'écrit sans dessin, en ajoutant la somme à elle-même écrite à l'envers : $S = 1 + 2 + \dots + n$ et $S = n + (n-1) + \dots + 1$ ; terme à terme, chaque paire vaut $n + 1$, et il y a $n$ paires, d'où $2S = n(n+1)$. C'est l'astuce attribuée au jeune Gauss pour $1 + 2 + \dots + 100 = 5050$. Plus généralement, la somme des termes d'une [[Suite arithmétique]] vaut nombre de termes $\times$ (premier + dernier) $/ 2$. [[Complément hors du cours|ⓘ]]

Côté algorithme, la boucle qui additionne $1, 2, \dots, n$ fait $n$ additions, alors que la formule donne le résultat en trois opérations, quel que soit $n$ : un raisonnement mathématique peut rendre un calcul beaucoup plus rapide (voir [[Complexité algorithmique]]). La formule se démontre aussi par [[Récurrence]], comme celle des tours de Hanoï plus bas. [[Complément hors du cours|ⓘ]]

## Langages et nombres flottants

- Si un problème est résoluble dans un langage de programmation, il l'est dans tous : les langages résolvent les mêmes problèmes.
- Cette équivalence a un nom : les langages usuels (Python, C, Java…) sont **Turing-complets**, c'est-à-dire qu'ils peuvent simuler une [[Machine de Turing]], donc calculer tout ce qu'elle calcule. La **thèse de Church-Turing** (années 1930) affirme que tout ce qui est calculable par un procédé mécanique l'est par une machine de Turing. Les langages diffèrent par la facilité d'écriture et la vitesse, pas par ce qu'ils peuvent calculer. À l'inverse, certains problèmes ne sont résolubles dans **aucun** langage : Turing a montré (1936) qu'aucun programme ne peut décider, pour tout programme et toute entrée, s'il finira par s'arrêter (problème de l'arrêt). [[Complément hors du cours|ⓘ]]
- En programmation, un [[Nombre à virgule flottante|float]] n'est pas un nombre réel. Exemple : $0.1 + 0.2 \ne 0.3$ (en Python, `0.1 + 0.2 == 0.3` vaut `False`). [[Erreurs du cours#^e-0-algo-maths|✎]]
- Pourquoi : un float est codé en binaire sur un nombre fini de bits (64 bits en double précision selon la [[Norme IEEE 754]] : un signe, un exposant, une mantisse de 52 bits). Or $0{,}1$ n'a pas d'écriture binaire finie ($0{,}1 = 0{,}000110011001\ldots_2$, la séquence 0011 se répète), de même que $1/3 = 0{,}333\ldots$ en base 10 : il est arrondi au flottant le plus proche, et les arrondis s'accumulent dans les calculs. Conséquence pratique : on ne compare jamais deux flottants avec `==`, mais à une tolérance près (`abs(a - b) < 1e-9`, ou `math.isclose(a, b)` en Python). [[Complément hors du cours|ⓘ]]

## Fractales

Une [[Fractale]] est un motif autosimilaire défini par récurrence (texte du dessin : « $u_0$ ; $u_1$ ; $u_2$ ; $u_n$ », étapes successives de construction).

- Propriété : les fractales ont un périmètre infini.
- Exemple : le flocon de Koch.
- Construction du flocon de Koch : on part d'un triangle équilatéral ($u_0$) ; à chaque étape, chaque segment est coupé en trois et son tiers central est remplacé par les deux côtés d'un petit triangle équilatéral pointant vers l'extérieur. Chaque segment devient 4 segments 3 fois plus courts, donc le périmètre est multiplié par $\frac{4}{3}$ : si le triangle de départ a un côté $a$, $P_n = 3a\left(\frac{4}{3}\right)^n$, qui tend vers l'infini (suite géométrique de raison $> 1$, voir [[Suite géométrique]]). L'aire, elle, reste finie : elle tend vers $\frac{8}{5}$ de l'aire du triangle de départ. Une courbe de longueur infinie entoure donc une surface finie. [[Complément hors du cours|ⓘ]]
- L'autosimilarité se mesure par la **dimension fractale** : une figure faite de $N$ copies d'elle-même réduites d'un facteur $k$ a pour dimension $\frac{\ln N}{\ln k}$. Pour un segment ($N = k$), on trouve 1 ; pour la courbe de Koch ($N = 4$, $k = 3$), $\frac{\ln 4}{\ln 3} \approx 1{,}26$ : plus qu'une ligne, moins qu'une surface. On trouve des formes approximativement fractales dans la nature (côtes, fougères, choux romanesco) ; le mot « fractale » a été forgé par Benoît Mandelbrot en 1975. [[Complément hors du cours|ⓘ]]
- En programmation, une fractale se dessine naturellement par [[Récursivité]] : tracer une courbe de Koch d'ordre $n$, c'est tracer quatre courbes d'ordre $n - 1$ trois fois plus petites, avec un cas de base (ordre 0 : un simple segment). [[Complément hors du cours|ⓘ]]

## Les tours de Hanoï

[[Tours de Hanoï]]. Problème : écrire un algorithme qui calcule le nombre minimal de coups pour déplacer $n$ disques.

Règles du jeu : trois piliers, $n$ disques de tailles différentes empilés du plus grand au plus petit sur le premier ; on déplace un seul disque à la fois (celui du sommet d'une pile), et on ne pose jamais un disque sur un plus petit. Le but est de reconstituer la pile sur le troisième pilier. [[Complément hors du cours|ⓘ]]

### Raisonnement

1. Il faut retirer tous les disques posés sur le grand disque $D$, puis déplacer $D$ sur le pilier final.
2. On réitère le même procédé, $D$ étant désormais le deuxième plus grand disque.
3. Le problème fait donc appel à la récursivité.

### Algorithme

```text
def coup.min() :
    Pour n = 0 → ne rien faire
    Pour n ≥ 1 :
        Déplacer n-1 disques du pilier 1 au pilier 2
        Déplacer le grand disque du 1 au 3
        Déplacer n-1 disques de 2 à 3
```

Le même algorithme en Python, qui affiche les coups et renvoie leur nombre : [[Complément hors du cours|ⓘ]]

```python
def hanoi(n, depart, arrivee, intermediaire):
    if n == 0:
        return 0                                          # cas de base : rien à faire
    c = hanoi(n - 1, depart, intermediaire, arrivee)      # dégager les n-1 disques
    print("disque", n, ":", depart, "->", arrivee)        # déplacer le grand disque
    c += 1
    c += hanoi(n - 1, intermediaire, arrivee, depart)     # remettre les n-1 disques dessus
    return c

hanoi(3, 1, 3, 2)   # affiche 7 coups et renvoie 7
```

Toute fonction récursive a besoin d'un **cas de base** (ici $n = 0$) qui arrête les appels, et chaque appel doit se rapprocher de ce cas (ici $n$ diminue de 1) ; sinon elle s'appelle à l'infini. [[Complément hors du cours|ⓘ]]

### Nombre de coups

Formule donnée par l'enseignant : $\text{coup.min}(n) = 2 \times \text{coup.min}(n-1) + 1$, soit la suite définie par récurrence $u_{n+1} = 2u_n + 1$. Texte du dessin : $f(0) = 0$ ; $f(n+1) = 2f(n) + 1$.

Pourquoi ce nombre est **minimal**, et pas seulement atteint : pour bouger le plus grand disque, les $n - 1$ autres doivent tous être sur un même autre pilier, ce qui coûte au moins $f(n-1)$ coups ; le grand disque bouge au moins une fois ; ensuite il faut encore ramener les $n - 1$ disques sur lui, soit au moins $f(n-1)$ coups. D'où $f(n) \ge 2f(n-1) + 1$, et l'algorithme atteint cette borne. [[Complément hors du cours|ⓘ]]

Forme générale : $u_n = 2^n - 1$.

Comment trouver cette forme avant de la démontrer : on calcule les premiers termes, $0, 1, 3, 7, 15, 31$, qui sont chacun une puissance de 2 moins 1. Méthode générale pour une suite $u_{n+1} = a u_n + b$ (suite arithmético-géométrique) : on pose $v_n = u_n + 1$ ; alors $v_{n+1} = 2u_n + 2 = 2v_n$, donc $(v_n)$ est une [[Suite géométrique]] de raison 2 et de premier terme $v_0 = 1$, d'où $v_n = 2^n$ et $u_n = 2^n - 1$. [[Complément hors du cours|ⓘ]]

Ce nombre croît exponentiellement : chaque disque ajouté double presque le travail. Pour 64 disques, la légende associée au jeu (inventé par le mathématicien Édouard Lucas en 1883), il faut $2^{64} - 1 \approx 1{,}8 \times 10^{19}$ coups ; à un coup par seconde, plus de 500 milliards d'années. Un algorithme en $2^n$ devient inutilisable dès que $n$ dépasse quelques dizaines (voir [[Complexité algorithmique]]). [[Complément hors du cours|ⓘ]]

### Démonstration par récurrence de $P(n) : f(n) = 2^n - 1$

- **Initialisation** : $f(0) = 2^0 - 1 = 0$.
- **Hérédité** : supposons $P(k)$ vraie. Alors
$$f(k+1) = 2f(k) + 1 = 2(2^k - 1) + 1 = 2 \cdot 2^k - 2 + 1 = 2^{k+1} - 1.$$
- **Conclusion** : si $P(k)$ est vraie, $P(k+1)$ l'est ; or $P(0)$ est vraie, donc la propriété est vraie pour tout entier $n \ge 0$. [[Erreurs du cours#^e-0-algo-maths|✎]]

Le principe de [[Récurrence]] fonctionne comme une chaîne de dominos : l'initialisation fait tomber le premier, l'hérédité garantit que chaque domino fait tomber le suivant, donc tous tombent. Les deux étapes sont indispensables : le problème des crayons ci-dessous montre ce qui arrive quand l'hérédité a un maillon manquant. Récurrence et [[Récursivité]] sont les deux faces de la même idée : l'une **démontre** une propriété en se ramenant au rang précédent, l'autre **calcule** un résultat en se ramenant à un problème plus petit. [[Complément hors du cours|ⓘ]]

## Le problème des crayons

[[Problème des crayons]]. Fausse démonstration par récurrence de $P_n$ : « dans un ensemble de $n$ crayons, tous les crayons sont de la même couleur ».

- **Initialisation** : pour $n = 1$, un ensemble d'un crayon n'a qu'une couleur.
- **Hérédité** : on suppose $P_k$ vraie. Dans un ensemble de $k+1$ crayons, l'hypothèse s'applique aux crayons 1 à $k$ et aux crayons 2 à $k+1$. Ces deux sous-ensembles partagent la couleur des crayons « du milieu », donc tous les $k+1$ crayons sont de même couleur.

Le résultat est absurde : la propriété est fausse pour tout $n \ge 2$. Il faut qu'il y ait des crayons du milieu pour que l'hérédité marche, or l'hérédité échoue de $k = 1$ à $k = 2$ : les deux groupes d'un crayon n'ont pas de crayon commun, et toute la chaîne tombe avec ce maillon. [[Erreurs du cours#^e-0-algo-maths|✎]]

## Le carré magique $3 \times 3$

[[Carré magique]] : grille $3 \times 3$ remplie avec les nombres de 1 à 9, où chaque ligne, chaque colonne et chaque diagonale a la même somme.

1. **Somme des entiers du carré** : $\dfrac{n(n+1)}{2} = \dfrac{9 \times 10}{2} = 45$.
2. **Somme selon une direction** : on divise la somme totale par 3, soit $15$.
3. **Valeur de la case centrale** : raisonnement du cours (dessin en vert, non conservé) : « si on vire ce qui est en vert, il ne reste que le carré du milieu, qui vaut $45 - 30 = 15$ ; or on compte 3 fois la case du milieu, donc $15/3 = 5$ ». La case centrale vaut **5**.
4. **Nombre de manières d'obtenir 15** avec trois nombres distincts de 1 à 9 : 8 manières.

| | |
|---|---|
| 1+5+9 | 2+6+7 |
| 1+6+8 | 3+4+8 |
| 2+4+9 | 3+5+7 |
| 2+5+8 | 4+5+6 |

5. **Combien y a-t-il de solutions ?** Réponse notée : « Bah 8 ig ».

L'étape 3 se justifie ainsi : les quatre lignes qui passent par le centre (la ligne du milieu, la colonne du milieu, les deux diagonales) totalisent $4 \times 15 = 60$. Elles contiennent chaque case de la grille une fois, sauf le centre $c$, compté quatre fois : $60 = 45 + 3c$, d'où $c = 5$. [[Complément hors du cours|ⓘ]]

Les 8 triplets du tableau correspondent exactement aux 8 alignements du carré (3 lignes, 3 colonnes, 2 diagonales), ce qui fixe la grille : 5 au centre est dans 4 triplets (4 alignements passent par le centre), les nombres pairs 2, 4, 6, 8 dans 3 triplets chacun (ils vont dans les coins), les impairs 1, 3, 7, 9 dans 2 (ils vont au milieu des bords). On obtient le carré ci-dessous, et les 8 solutions sont ses images par les 4 rotations et les 4 symétries du carré : il n'existe qu'**un seul** carré magique $3 \times 3$ à symétrie près, connu en Chine depuis l'Antiquité sous le nom de *Lo Shu*. [[Complément hors du cours|ⓘ]]

| | | |
|---|---|---|
| 2 | 7 | 6 |
| 9 | 5 | 1 |
| 4 | 3 | 8 |

Plus généralement, un carré magique $n \times n$ rempli avec les nombres de 1 à $n^2$ a pour somme magique $\dfrac{n(n^2+1)}{2}$ (la somme totale $\frac{n^2(n^2+1)}{2}$ divisée par $n$ lignes) : 15 pour $n = 3$, 34 pour $n = 4$. [[Complément hors du cours|ⓘ]]
