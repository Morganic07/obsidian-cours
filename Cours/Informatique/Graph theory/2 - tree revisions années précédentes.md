---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Résumé de [[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Diaporama « Arbres » (34 diapositives) du cours d'algorithmique procédurale II de 1re année d'ingénieur (ING1-GI), CY Tech, 2020-2021 : un support d'une année précédente, rangé par l'utilisatrice dans les suppléments du chapitre 2, [[2 - tree]]. Il révise le côté structure de données des arbres, quand [[2 - tree]] traite leur côté graphe (forêts, arbres couvrants).

## Idée générale

Définitions d'un [[Arbre (théorie des graphes)|arbre]] et vocabulaire, [[Hauteur d'un arbre|hauteur]] en fonction de la taille, [[Parcours en profondeur|parcours en profondeur]] ([[Parcours préfixe|préfixe]], [[Parcours postfixe|postfixe]], [[Parcours infixe|infixe]]) et [[Parcours en largeur|en largeur]], opérations d'un [[Type abstrait de données|type abstrait]] « arbre » (k-aire, puis binaire) décrites par leurs [[Précondition et postcondition|préconditions et postconditions]], et enfin l'[[Arbre binaire de recherche]] : recherche, insertion, suppression.

## Définitions

**Définition de théorie des graphes.** Un arbre est un graphe ([[Graphe orienté|orienté]] ou [[Graphe non orienté|non]]), [[Graphe connexe|connexe]] et sans [[Cycle (graphe)|cycle]].

Pour un graphe orienté, cette définition se lit sur le [[Graphe sous-jacent|graphe sous-jacent]] (on oublie le sens des arcs) : connexe et sans cycle, il a la forme d'un arbre. Elle ne suffit pas à faire un arbre enraciné : les arcs 1 → 3 et 2 → 3 forment un tel graphe, mais aucun sommet n'atteint tous les autres. D'où la définition de l'arbre enraciné ci-dessous. Un arbre à $n$ sommets a toujours $n - 1$ arêtes (ou arcs). [[Complément hors du cours|ⓘ]]

**Définition récursive.** Un arbre est un ensemble fini, non vide, de nœuds : l'un d'eux est la racine, et les autres se répartissent en $m \ge 0$ ensembles disjoints qui sont eux-mêmes des arbres, les [[Sous-arbre|sous-arbres]] de la racine, à laquelle chacun est relié par un lien ou un [[Pointeur et adresse mémoire|pointeur]]. [[Erreurs du cours#^e-2-tree-revisions-annees-precedentes|✎]]

Cette définition, sur laquelle reposent les algorithmes [[Récursivité|récursifs]] du cours, n'est pas circulaire : chaque sous-arbre a strictement moins de nœuds que l'arbre, et la récursion s'arrête sur les arbres réduits à un nœud. Beaucoup de cours admettent aussi l'arbre vide (sans nœud) comme cas de base, ce qui simplifie l'écriture des arbres binaires (un fils absent est un arbre vide). [[Complément hors du cours|ⓘ]]

Le cours distingue deux sortes d'arbres :
- **arbre non enraciné** : il n'y a ni ordre ni hiérarchie entre ses éléments. Exemple : 9 sommets, 1 relié à 2, 9 et 3, 3 relié à 4, 4 relié à 5, 6, 7 et 8 ;
- **[[Arborescence (graphe)|arbre enraciné]]** : arbre hiérarchique dans lequel on peut établir des niveaux. Un nœud ([[Sommet et arête|sommet]]) spécial, la **racine**, est tel qu'il existe un [[Chemin (graphe)|chemin simple]] de la racine à chaque nœud. Le cours considère toujours un arbre enraciné comme un graphe orienté (arcs du père vers les fils). Exemple : racine 1, fils 2 et 3 ; 3 a pour fils 4 et 5 ; 4 a pour fils 6, 7 et 8.

Ce chemin de la racine à un nœud est unique, puisque deux chemins différents formeraient un cycle dans le graphe sous-jacent. Retirer la racine d'un arbre enraciné laisse une [[Forêt (graphe)|forêt]], celle de ses sous-arbres. [[Complément hors du cours|ⓘ]]

## Terminologie

Dans un [[Arborescence (graphe)|arbre enraciné]], vu comme [[Graphe orienté|graphe orienté]] (voir [[Vocabulaire des arbres]] et [[Sous-arbre]]) :
- **nœud externe** ou **feuille** : nœud qui n'a pas d'arc sortant ;
- **nœud interne** : nœud qui n'est pas externe ;
- **[[Degré d'un sommet|degré]] d'un nœud** : nombre d'arcs sortants du nœud, c'est-à-dire de ses fils ;
- **nœuds frères** (ou sœurs) : nœuds qui ont le même parent ;
- **ancêtre** : un nœud $u$ est un ancêtre de $w$ si $w$ est dans l'arbre enraciné en $u$ ;
- **descendant** : $w$ est un descendant de $u$ si $w$ est dans l'arbre enraciné en $u$.

Ce degré ne compte que les fils : dans le graphe non orienté sous-jacent, un nœud autre que la racine a en plus une arête vers son père, et son degré y vaut un de plus. Avec la définition du cours, chaque nœud est ancêtre et descendant de lui-même ; on parle d'ancêtre **propre** pour exclure ce cas. [[Complément hors du cours|ⓘ]]

**Arbres ordonnés et numérotés.**
- **[[Arbre ordonné]]** : il existe un ordre entre les enfants des nœuds internes (un premier, un deuxième…).
- **[[Arbre numéroté]]** : les enfants de chaque nœud sont étiquetés par des entiers positifs distincts ; un arbre numéroté est ordonné (numéroté → ordonné).
  - **$i$-ème enfant absent** : aucun enfant n'est étiqueté par $i$. La figure de la diapositive 6 reprend l'arbre de la diapositive 7 (ci-dessous) sans le nœud 3 ni ses descendants : la racine 1 n'a plus que les enfants 2 et 4, entre lesquels manque un enfant.
  - **[[Arbre m-aire|Arbre k-aire]]** (ou d'arité $k$) : arbre dont les nœuds ont au plus $k$ fils.
  - Un **[[Arbre binaire|arbre binaire]]** est un arbre d'arité 2.

La différence compte en arbre binaire : un nœud qui n'a qu'un fils doit dire s'il est gauche ou droit. Les deux arbres « racine A, fils gauche B » et « racine A, fils droit B » sont le même arbre ordonné (un seul enfant), mais deux arbres binaires distincts. [[Complément hors du cours|ⓘ]]

**Mesures.**
- **Taille** d'un arbre : nombre de ses nœuds.
- **Profondeur** d'un nœud : distance (nombre d'arcs) du chemin qui relie la racine au nœud ; la racine est à la profondeur 0.
- **[[Hauteur d'un arbre]]** : profondeur maximale de ses nœuds.

![[2 - tree revisions années précédentes - p8.jpg]]
*Figure (diapositive 7) : arbre ternaire de taille 16. La racine 1 a pour fils 2, 3 et 4 ; 2 → 5 → 10, 11 ; 3 → 6, 7, et 7 → 12, 13, 14 ; 4 → 8, 9, et 8 → 15, 16. Sa hauteur vaut $h = 3$ (profondeur de 10 à 16).*

**Théorème.** Soit un arbre $k$-aire ($k \ge 2$) de hauteur $h$ et de taille $n \ge 1$. Alors [[Erreurs du cours#^e-2-tree-revisions-annees-precedentes|✎]]
- $h = n - 1$ dans le pire des cas (hauteur la plus grande : chaque nœud interne a un seul fils) ;
- $h = \lceil \log_k((k-1)n + 1) \rceil - 1$ dans le meilleur des cas, soit $h = \lfloor \log_2 n \rfloor$ pour un arbre binaire.

Preuve du meilleur cas : au plus $k^p$ nœuds ont la profondeur $p$, donc un arbre de hauteur $h$ a au plus $1 + k + \dots + k^h = \frac{k^{h+1} - 1}{k - 1}$ nœuds (somme d'une [[Suite géométrique|suite géométrique]]). Il faut donc $k^{h+1} \ge (k-1)n + 1$, soit $h \ge \log_k((k-1)n+1) - 1$ ([[Logarithme|logarithme]] en base $k$), et la plus petite hauteur entière est l'arrondi au-dessus ([[Partie entière|partie entière]] supérieure), atteinte en remplissant chaque niveau avant le suivant. Sur la figure, $n = 16$ et $k = 3$ donnent $\lceil \log_3 33 \rceil - 1 = 4 - 1 = 3$ : cet arbre a la plus petite hauteur possible. [[Complément hors du cours|ⓘ]]

Un arbre binaire de hauteur minimale a $\lfloor \log_2 n \rfloor + 1$ **niveaux** : c'est sa hauteur si l'on compte les nœuds d'une branche plutôt que ses arcs (racine à la profondeur 1), convention que suivent certains manuels. Retenir l'ordre de grandeur : la hauteur d'un arbre va de $\log n$ (arbre « touffu », [[Arbre équilibré|équilibré]]) à $n$ (arbre [[Arbre dégénéré|dégénéré]], qui n'est qu'une [[Liste chaînée|liste]]), et le coût des opérations suit. [[Complément hors du cours|ⓘ]]

## Parcours

Un **parcours** est un [[Algorithme|algorithme]] qui visite tous les nœuds d'un arbre : il appelle une méthode, [[Fonction et procédure|fonction ou procédure]] sur tous les nœuds (ou les [[Sous-arbre|sous-arbres]]).
- **[[Parcours en profondeur]]** : si l'arbre n'est pas vide, le parcours de l'un des sous-arbres est terminé avant que ne commence celui de l'autre. On explore une branche jusqu'au bout avant de passer à la suivante (les fils avant les frères).
- **[[Parcours en largeur]]** : on procède par niveaux croissants. On explore les nœuds un par un sur un même niveau, puis on passe au niveau suivant (les frères avant les fils).

On considère toujours un parcours de gauche à droite. Les exemples des diapositives 10 à 13 portent sur l'[[Arbre binaire|arbre binaire]] : 1 → 2, 8 ; 2 → 3, 6 ; 3 → 4, 5 ; 6 → 7 (fils droit) ; 8 → 9, 10.

![[2 - tree revisions années précédentes - p12.jpg]]
*Figure (diapositive 10) : l'arbre des exemples de parcours, ses nœuds numérotés dans l'ordre préfixe ; les chiffres manuscrits sont des annotations de l'utilisatrice.*

### Parcours en profondeur

| Parcours | Règle | Arbre binaire | Ordre sur l'exemple |
|---|---|---|---|
| **[[Parcours préfixe\|Préfixe]]** | chaque nœud est visité avant ses fils : la racine, puis le parcours préfixe des sous-arbres de gauche à droite | R G D (racine, gauche, droit) | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| **[[Parcours postfixe\|Postfixe]]** (ou suffixe) | chaque nœud est visité après chacun de ses fils : le parcours postfixe des sous-arbres de gauche à droite, puis la racine | G D R | 4, 5, 3, 7, 6, 2, 9, 10, 8, 1 |
| **[[Parcours infixe\|Infixe]]** (ou symétrique) | arbre binaire seulement : chaque nœud est visité après son fils gauche et avant son fils droit (sous-arbre gauche, racine, sous-arbre droit) | G R D | 4, 3, 5, 2, 6, 7, 1, 9, 8, 10 |

Dans l'ordre infixe, 7 vient après 6 parce que 7 est le fils **droit** de 6 ; fils gauche, il passerait avant lui.

En [[Pseudo-code|pseudo-code]], les trois parcours ne diffèrent que par la place de la visite par rapport aux appels [[Récursivité|récursifs]] (opérations du cours, voir plus bas) : [[Complément hors du cours|ⓘ]]

```
Procédure prefixe (a : Arbre d'Élément)
    visiter(racine(a))
    Pour i de 1 à degre(a) faire
        prefixe(recEnfant(a, i))
    FinPour

Procédure postfixe (a : Arbre d'Élément)
    Pour i de 1 à degre(a) faire
        postfixe(recEnfant(a, i))
    FinPour
    visiter(racine(a))

Procédure infixe (a : ArbreBinaire d'Élément)
    Si existeFilsGauche(a) alors infixe(filsGauche(a)) FinSi
    visiter(racine(a))
    Si existeFilsDroit(a) alors infixe(filsDroit(a)) FinSi
```

Chaque nœud est visité une fois et chaque arc suivi une fois : un parcours coûte $\Theta(n)$ en temps ([[Complexité algorithmique|complexité]] linéaire, voir [[Comparaison asymptotique]]). La [[Pile d'exécution|pile d'exécution]] contient au plus $h + 1$ appels en cours, d'où une mémoire en $O(h)$ : de $O(\log n)$ pour un arbre [[Arbre équilibré|équilibré]] à $O(n)$ pour un arbre [[Arbre dégénéré|dégénéré]] ([[Hauteur d'un arbre|hauteur]] $h$). [[Complément hors du cours|ⓘ]]

Sans récursivité, le parcours préfixe s'écrit avec une [[Pile et file|pile]] explicite : empiler la racine ; tant que la pile n'est pas vide, dépiler un nœud, le visiter, puis empiler ses fils **de droite à gauche**, pour que le fils gauche sorte le premier. Remplacer la pile par une file, en y ajoutant les fils de gauche à droite, donne le parcours en largeur ci-dessous. [[Complément hors du cours|ⓘ]]

Usages : le parcours postfixe sert dès qu'un nœud a besoin du résultat de ses fils (calculer la hauteur, $h = 1 + \max$ des hauteurs des fils ; libérer la mémoire d'un arbre ; donner la taille d'un répertoire dans un [[Système de fichiers|système de fichiers]]) ; le préfixe sert à copier ou afficher une hiérarchie (la commande `tree` d'une [[Arborescence des répertoires Linux|arborescence de répertoires]]). Sur un **arbre d'expression**, dont les feuilles sont des nombres et les nœuds internes des opérateurs, les parcours préfixe, infixe et postfixe donnent la [[Notation polonaise|notation polonaise]], l'écriture usuelle (avec parenthèses) et la notation polonaise inverse. [[Complément hors du cours|ⓘ]]

Pour un arbre binaire aux étiquettes distinctes, l'ordre préfixe et l'ordre infixe suffisent à reconstruire l'arbre : la première étiquette du préfixe est la racine, et sa place dans l'infixe sépare le sous-arbre gauche du droit. Le préfixe et le postfixe seuls n'y suffisent pas (on ne sait pas si un fils unique est gauche ou droit). [[Complément hors du cours|ⓘ]]

### Parcours en largeur

Le parcours en largeur se réalise à l'aide d'une **[[Pile et file|file]]** :
1. mettre la racine dans la file ;
2. tant que la file n'est pas vide : récupérer en tête de file le nœud à traiter, le visiter, ajouter ses fils dans la file.

Parcours sur l'exemple : 1, 2, 8, 3, 6, 9, 10, 4, 5, 7 (niveau 0 : 1 ; niveau 1 : 2, 8 ; niveau 2 : 3, 6, 9, 10 ; niveau 3 : 4, 5, 7).

Contenu de la file au fil de l'algorithme, tête à gauche : [1] → visite 1 → [2, 8] → visite 2 → [8, 3, 6] → visite 8 → [3, 6, 9, 10] → visite 3 → [6, 9, 10, 4, 5] → visite 6 → [9, 10, 4, 5, 7] → visites 9, 10, 4, 5 → [7] → visite 7 → [ ]. Le principe FIFO (premier entré, premier sorti) garantit qu'un niveau sort entièrement avant le suivant. Chaque nœud entre et sort une fois de la file : coût $\Theta(n)$, et la file ne contient jamais que des nœuds de deux niveaux consécutifs (la fin du niveau en cours, le début du suivant). [[Complément hors du cours|ⓘ]]

En pseudo-code, avec les opérations du cours et celles d'une file (`enfiler`, `defiler`, `estVide`) : [[Complément hors du cours|ⓘ]]

```
Procédure largeur (a : Arbre d'Élément)
    f ← file vide ; enfiler(f, a)
    TantQue non estVide(f) faire
        b ← defiler(f) ; visiter(racine(b))
        Pour i de 1 à degre(b) faire enfiler(f, recEnfant(b, i)) FinPour
    FinTantQue
```

Le même algorithme, avec un marquage des sommets déjà vus, parcourt un graphe quelconque (voir [[4 - oriented graphs]]) ; dans un arbre, il est inutile, chaque nœud n'ayant qu'un père. Le parcours en largeur donne aussi la profondeur de chaque nœud (celle de son père plus 1). [[Complément hors du cours|ⓘ]]

## Opérations sur un arbre k-aire

Le cours décrit un arbre comme un [[Type abstrait de données|type abstrait]], `Arbre d'Élément`, par la signature de ses opérations ([[Fonction et procédure|fonctions et procédures]]) sur un [[Arbre m-aire|arbre k-aire]] ; chacune a une **précondition** (ce qui doit être vrai avant l'appel) et une **postcondition** (ce qui est vrai après). (S) et (E/S) sont les modes de [[Passage de paramètres|passage des paramètres]] : sortie, entrée-sortie. Voir [[Précondition et postcondition]].

| Opération | Précondition | Postcondition |
|---|---|---|
| Procédure `creerArbre(a : Arbre d'Élément (S), r : Élément)` | — | crée l'arbre `a` de racine `r`, sans fils |
| Procédure `modifierRacine(a (E/S), r : Élément)` | `a` initialisé | remplace la valeur de la racine de `a` par `r` |
| Procédure `ajouterFeuille(a (E/S), e : Élément)` | `a` initialisé | ajoute à `a` une feuille de valeur `e` |
| Procédure `supprimerFeuille(a (E/S))` | `a` initialisé, et `estFeuille(a)` | la feuille `a` est supprimée et n'existe plus pour son père |
| Fonction `estFeuille(a) : booléen` | `a` initialisé | renvoie VRAI si `a` n'a pas de fils |
| Fonction `racine(a) : Élément` | `a` initialisé | renvoie la valeur de la racine de `a` |
| Fonction `degre(a) : entier` | `a` initialisé | renvoie le nombre de fils de `a` |
| Fonction `recEnfant(a, pos : entier) : Arbre d'Élément` | `a` initialisé, et $1 \le pos \le$ `degre(a)` | renvoie le fils de `a` à la position `pos` |

Les fonctions renvoient un résultat (un [[Booléen|booléen]], un [[Type entier|entier]], un élément ou un arbre) sans modifier l'arbre ; les procédures le modifient. Ne passer que par ces opérations pour manipuler l'arbre, c'est l'[[Encapsulation (programmation)|encapsulation]] : on peut changer la représentation (tableau de fils, liste de fils, « fils aîné, frère suivant ») sans toucher aux algorithmes qui l'utilisent. [[Complément hors du cours|ⓘ]]

Appeler une opération hors de sa précondition (par exemple `recEnfant(a, 3)` sur un nœud de degré 2) est une faute de l'appelant : l'opération ne promet rien. C'est la logique du contrat, qui sert aussi à prouver la [[Correction d'un algorithme|correction d'un algorithme]] ; en C, on la vérifie pendant le développement avec `assert`. [[Complément hors du cours|ⓘ]]

## Opérations sur un arbre binaire

Cas particulier de l'[[Arbre binaire|arbre binaire]], le [[Type abstrait de données|type]] `ArbreBinaire d'Élément` ([[Précondition et postcondition|préconditions et postconditions]]) :

| Opération | Précondition | Postcondition |
|---|---|---|
| Procédure `creerArbreBinaire(a (S), r : Élément)` | — | crée l'arbre binaire `a` de racine `r`, sans fils droit ni gauche |
| Procédure `modifierRacine(a (E/S), r : Élément)` | `a` initialisé | remplace la valeur de la racine de `a` par `r` |
| Procédure `ajouterFilsDroit(a (E/S), r : Élément)` | `a` initialisé, sans fils droit | ajoute à `a` un fils droit de racine `r` |
| Procédure `ajouterFilsGauche(a (E/S), r : Élément)` | `a` initialisé, sans fils gauche | ajoute à `a` un fils gauche de racine `r` |
| Procédure `supprimerFilsDroit(a (E/S))` | `a` initialisé, ayant un fils droit qui est une feuille | `a` n'a plus de fils droit |
| Procédure `supprimerFilsGauche(a (E/S))` | `a` initialisé, ayant un fils gauche qui est une feuille | `a` n'a plus de fils gauche |
| Fonction `existeFilsDroit(a) : booléen` | `a` initialisé | VRAI si `a` a un fils droit, FAUX sinon |
| Fonction `existeFilsGauche(a) : booléen` | `a` initialisé | VRAI si `a` a un fils gauche, FAUX sinon |
| Fonction `filsDroit(a) : ArbreBinaire` | `a` initialisé, ayant un fils droit | renvoie le fils droit de `a` |
| Fonction `filsGauche(a) : ArbreBinaire` | `a` initialisé, ayant un fils gauche | renvoie le fils gauche de `a` [[Erreurs du cours#^e-2-tree-revisions-annees-precedentes\|✎]] |
| Fonction `racine(a) : Élément` | `a` initialisé | renvoie la racine de `a` |
| Fonction `estFeuille(a) : booléen` | `a` initialisé | VRAI si `a` est une feuille, FAUX sinon |

En C, un nœud d'arbre binaire se représente par une [[Structure (struct)|structure]] qui contient la valeur et deux pointeurs, `gauche` et `droit`, valant [[Pointeur NULL|NULL]] quand le fils est absent ; `creerArbreBinaire` et `ajouterFils…` allouent les nœuds par [[Allocation dynamique|allocation dynamique]] (`malloc`), et la suppression les libère (`free`). Un arbre binaire quasi-complet se range aussi sans pointeurs dans un [[Tableau (programmation)|tableau]], fils de la case $i$ en $2i$ et $2i+1$, comme le [[Tas binaire|tas binaire]]. [[Complément hors du cours|ⓘ]]

Le nombre de formes d'arbres binaires à $n$ nœuds est le $n$-ième [[Nombre de Catalan|nombre de Catalan]], $C_n = \frac{1}{n+1}\binom{2n}{n}$ ([[Coefficient binomial|coefficient binomial]]) : 1, 1, 2, 5, 14, 42… pour $n = 0, 1, 2, 3, 4, 5$. Il vérifie la récurrence $C_{n+1} = \sum_{i=0}^{n} C_i\,C_{n-i}$ : une racine, un sous-arbre gauche à $i$ nœuds, un sous-arbre droit à $n - i$ nœuds ([[Dénombrement|dénombrement]]). [[Complément hors du cours|ⓘ]]

## Arbre binaire de recherche : introduction

Dans un [[Arbre binaire|arbre binaire]] quelconque, la recherche d'un élément a une [[Complexité algorithmique|complexité]] **[[Classe de complexité|linéaire]]** en le nombre de nœuds : il faut parcourir tous les nœuds pour trouver l'élément. Il n'y a aucun gain par rapport à une [[Recherche séquentielle|recherche dans une liste]]. Comment optimiser la recherche dans un arbre ?

**Définition.** Un arbre binaire $a$ est un **[[Arbre binaire de recherche|arbre binaire de recherche]]** (ABR) si et seulement si :
- les valeurs du [[Sous-arbre|sous-arbre]] gauche sont $<$ `racine(a)` ;
- les valeurs du sous-arbre droit sont $>$ `racine(a)` ;
- tout sous-arbre de $a$ est un ABR.

Exemple : racine 8 ; fils 3 et 10 ; 3 a pour fils 1 et 6, 10 a pour fils droit 14 ; 6 a pour fils 4 et 7, 14 a pour fils gauche 13.

**Remarque.** Selon la mise en œuvre de l'ABR, on interdit ou non des nœuds de valeur égale. Le cours travaille avec des arbres à éléments uniques.

Les valeurs doivent appartenir à un ensemble muni d'un ordre total ([[Relation d'ordre|relation d'ordre]]), pour que deux valeurs soient toujours comparables. La troisième condition est essentielle : vérifier seulement chaque père contre ses deux fils ne suffit pas, car toute valeur du sous-arbre gauche doit être plus petite que la racine, pas seulement le fils gauche. [[Complément hors du cours|ⓘ]]

Propriété fondamentale : le **parcours infixe d'un ABR donne ses valeurs dans l'ordre croissant** (sur l'exemple : 1, 3, 4, 6, 7, 8, 10, 13, 14). Réciproquement, un arbre binaire est un ABR si et seulement si son parcours infixe est strictement croissant. Insérer $n$ valeurs puis lire l'infixe est donc un tri. [[Complément hors du cours|ⓘ]]

## ABR : traitements

### Recherche

**Principe.** On compare la valeur cherchée à la racine :
- si elle est inférieure, on recherche récursivement dans le sous-arbre gauche ;
- si elle est supérieure, dans le sous-arbre droit.

La recherche s'arrête quand la racine est égale à la valeur cherchée, ou quand le sous-arbre gauche (ou droit) n'existe pas : la valeur n'est pas dans l'arbre.

Exemple sur l'arbre de la définition : chercher 7 compare 8 (aller à gauche), 3 (à droite), 6 (à droite), 7 (trouvé), soit 4 comparaisons ; chercher 5 passe par 8, 3, 6, 4, et 4 n'a pas de fils droit : 5 est absent. C'est l'idée de la [[Recherche dichotomique|recherche dichotomique]] dans un tableau trié, chaque comparaison écartant un sous-arbre entier. [[Complément hors du cours|ⓘ]]

En pseudo-code, avec les opérations du type `ArbreBinaire` : [[Complément hors du cours|ⓘ]]

```
Fonction rechercher (a : ArbreBinaire d'Élément, x : Élément) : booléen
    Si x = racine(a) alors retourner VRAI
    Sinon Si x < racine(a) alors
        Si existeFilsGauche(a) alors retourner rechercher(filsGauche(a), x)
        Sinon retourner FAUX FinSi
    Sinon
        Si existeFilsDroit(a) alors retourner rechercher(filsDroit(a), x)
        Sinon retourner FAUX FinSi
    FinSi
```

La récursion est terminale (l'appel récursif est la dernière action) : elle se réécrit en simple [[Boucle (programmation)|boucle]] `TantQue` qui descend d'un niveau à chaque tour. [[Complément hors du cours|ⓘ]]

Le **minimum** d'un ABR est le nœud le plus à gauche (descendre par les fils gauches tant qu'il en existe), le **maximum** le plus à droite ; tous deux en $O(h)$ (voir [[Recherche du minimum et du maximum]]). Le **successeur** d'un nœud qui a un fils droit est le minimum de son sous-arbre droit. [[Complément hors du cours|ⓘ]]

### Complexité

Le nombre d'appels [[Récursivité|récursifs]] dépend de la [[Hauteur d'un arbre|hauteur]] de l'[[Arbre binaire de recherche|ABR]] ([[Complexité algorithmique|complexité]]) :
- meilleur des cas : $O(\log n)$, si l'arbre est « équilibré » ;
- pire des cas : $O(n)$, si l'arbre est « dégénéré ».

Ces cas portent sur la **forme de l'arbre** : la recherche coûte $O(h)$, et $h$ va de $\lfloor \log_2 n \rfloor$ (arbre [[Arbre équilibré|équilibré]]) à $n - 1$ (arbre [[Arbre dégénéré|dégénéré]], par exemple obtenu en insérant des valeurs déjà triées). Si les valeurs arrivent dans un ordre aléatoire, la hauteur est en moyenne $O(\log n)$. Pour **garantir** $O(\log n)$ quoi qu'il arrive, on rééquilibre l'arbre après chaque insertion ou suppression : [[Arbre AVL]] (hauteurs des deux sous-arbres de chaque nœud différant d'au plus 1), [[Arbre rouge-noir]] (utilisé par `std::map` de la [[Bibliothèque standard du C++|bibliothèque standard du C++]] et `TreeMap` de Java pour réaliser un [[Tableau associatif|tableau associatif]]). Sur disque, les bases de données emploient des [[B-arbre|B-arbres]], arbres équilibrés à grand nombre de fils. [[Complément hors du cours|ⓘ]]

Comparé à une [[Table de hachage|table de hachage]] (accès en $O(1)$ en moyenne), un ABR équilibré est plus lent, mais garde les clés **ordonnées** : minimum, maximum, successeur, parcours trié et recherche d'intervalle restent faciles. [[Complément hors du cours|ⓘ]]

### Insertion

**Principe.** On ajoute un nouvel élément **en [[Vocabulaire des arbres|feuille]]**, en respectant les propriétés d'un [[Arbre binaire de recherche|ABR]] :
- si l'élément est déjà dans l'arbre, on ne l'ajoute pas ;
- sinon, on descend au bout de l'unique branche que suivrait sa recherche, et on y ajoute l'élément.

**Exemples.**
- Ajout de 2 : $2 < 8$, puis $2 < 3$, puis $2 > 1$ ; 1 n'a pas de fils droit : 2 devient le fils droit de 1.
- Ajout de 9 : $9 > 8$, puis $9 < 10$ ; 10 n'a pas de fils gauche : 9 devient le fils gauche de 10.

![[2 - tree revisions années précédentes - p32.jpg]]
*Figure (diapositive 30) : à gauche, l'ABR après l'ajout de 2 (en rose, fils droit de 1) ; à droite, après l'ajout de 9 (fils gauche de 10).*

L'insertion coûte une recherche plus une création de feuille, soit $O(h)$. L'ordre d'insertion fixe la forme de l'arbre : 1, 2, 3, 4… donne un arbre dégénéré, alors qu'insérer d'abord la médiane, puis les médianes de chaque moitié, donne un arbre équilibré. [[Complément hors du cours|ⓘ]]

### Suppression

**Principe.** Supprimer un élément n'est pas immédiat : il ne faut pas compromettre la [[Relation d'ordre|relation d'ordre]] entre les éléments qui restent de l'[[Arbre binaire de recherche|ABR]]. Trois cas ; chaque exemple part de l'arbre obtenu après les deux insertions (racine 8 ; 3, 10 ; 1, 6, 9, 14 ; 2, 4, 7, 13) :
1. **Feuille** : trivial, aucune réorganisation n'est nécessaire. Exemple : supprimer 13, 14 n'a plus de fils.
2. **Un seul fils** : trivial, on remplace le nœud par son fils. Exemple : supprimer 1, dont le seul fils 2 prend la place (2 devient fils gauche de 3).
3. **Deux fils** : on remplace le nœud par son **successeur** (le plus petit élément de son sous-arbre droit) ou par son **prédécesseur** (le plus grand de son sous-arbre gauche). Exemple : supprimer la racine 8, remplacée par 9, le plus petit élément du sous-arbre droit ; 10 n'a plus de fils gauche.

![[2 - tree revisions années précédentes - p36.jpg]]
*Figure (diapositive 34) : suppression de la racine 8, qui a deux fils ; son successeur 9 (en vert) prend sa place.*

Dans le cas 3, le successeur n'a jamais de fils gauche (ce fils serait plus petit que lui, donc un meilleur candidat) : on le retire par le cas 1 ou 2, et tout le sous-arbre gauche reste plus petit que lui, tout le sous-arbre droit plus grand. Avec le prédécesseur, c'est 7 qui serait monté à la racine et 6 aurait perdu son fils droit. Coût de la suppression : $O(h)$. [[Complément hors du cours|ⓘ]]

## Usages des arbres

Au-delà du cours, les [[Arbre (théorie des graphes)|arbres]] sont partout en informatique : [[Système de fichiers|systèmes de fichiers]] (répertoires et fichiers), documents [[Langage de balisage|XML et HTML]] (arbre DOM), [[Notation polonaise|arbres d'expression]] des compilateurs, [[Codage de Huffman|codage de Huffman]] (arbre binaire des codes), [[Arbre de décision|arbres de décision]] en apprentissage automatique, [[Tas binaire|tas binaire]] pour réaliser une [[File de priorité|file de priorité]] (utilisée par l'[[Algorithme de Dijkstra|algorithme de Dijkstra]]), et index des [[Système de gestion de base de données|bases de données]] en [[B-arbre|B-arbres]]. [[Complément hors du cours|ⓘ]]
