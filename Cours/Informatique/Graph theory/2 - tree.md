---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Chp2 - tree.docx|Chp2 - tree]]"]
maj: 2026-11-08
complet: true
enrichi: 2026-11-08
---

Résumé de [[Raw/Year 4/graph theory/Chp2 - tree.docx|Chp2 - tree]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Cours en anglais (pseudo-code en français). Images non ouvertes : lues par leur transcription.

## Idée générale

Arbres et forêts, arbre couvrant, et recherche d'un arbre couvrant de poids minimum par l'algorithme de Kruskal. Voir [[Arbre couvrant minimal]].

## Arbre

**Définition.** Un **arbre** (*tree*) est un [[Graphe non orienté|graphe non orienté]] **connexe** et **acyclique** (sans cycle). Voir [[Arbre (théorie des graphes)]].

**Propositions 1 et 2.**
- Tout arbre est un [[Graphe simple|graphe simple]].
- Toute [[Chaîne (graphe)|chaîne élémentaire]] est un arbre.

Pourquoi un arbre est simple : une boucle est un cycle de longueur 1, et deux arêtes parallèles entre $u$ et $v$ forment un cycle de longueur 2 ($u, e, v, e', u$) ; un graphe acyclique n'a donc ni l'une ni les autres. Pourquoi une chaîne élémentaire est un arbre : ses sommets sont reliés de proche en proche (connexe), et comme elle ne repasse jamais par un sommet, elle ne peut pas se refermer (acyclique). [[Complément hors du cours|ⓘ]]

Pour un graphe $G$ à $n$ sommets, les propriétés suivantes sont **équivalentes** ; chacune peut servir de définition d'un arbre : [[Complément hors du cours|ⓘ]]
1. $G$ est connexe et acyclique ;
2. $G$ est connexe et a $n - 1$ arêtes ;
3. $G$ est acyclique et a $n - 1$ arêtes ;
4. deux sommets quelconques sont reliés par une **unique** chaîne élémentaire ;
5. $G$ est connexe, et la suppression de n'importe quelle arête le déconnecte (toute arête est un [[Pont (graphe)|pont]]) ;
6. $G$ est acyclique, et l'ajout de n'importe quelle arête crée un cycle.

Tout arbre à au moins 2 sommets a **au moins deux feuilles** (sommets de [[Degré d'un sommet|degré]] 1) : les deux extrémités d'une plus longue chaîne élémentaire en sont. C'est l'outil des démonstrations par [[Récurrence|récurrence]] sur les arbres : on retire une feuille et son arête, il reste un arbre à $n - 1$ sommets. [[Complément hors du cours|ⓘ]]

![[Chp2 - tree - image2.png]]
*Figure : trois exemples d'arbres — une chaîne élémentaire de 4 sommets alignés ; une étoile (un sommet central relié à 3 feuilles) ; deux sommets internes reliés entre eux, portant 2 et 3 feuilles.*

## Forêt et pont

- **Forêt** (*forest*) : graphe non orienté **acyclique**. Voir [[Forêt (graphe)]].
- Toute [[Graphe connexe|composante connexe]] d'une forêt est un arbre.
- **Pont** (*bridge*) : soit $G = (V, E, \gamma)$ ; un pont de $G$ est une arête $e$ telle que $G - e$ a **une composante connexe de plus** que $G$. Voir [[Pont (graphe)]].

Note de l'étudiante : un arbre est une forêt ; une forêt n'est pas (forcément) un arbre.

Une forêt à $n$ sommets et $c$ composantes connexes a exactement $n - c$ arêtes : chaque composante, arbre à $n_i$ sommets, en a $n_i - 1$, et $\sum_i (n_i - 1) = n - c$. [[Complément hors du cours|ⓘ]]

Une arête est un pont **si et seulement si elle n'appartient à aucun cycle** : si elle est sur un cycle, le reste du cycle relie encore ses extrémités après sa suppression ; sinon, plus rien ne les relie. D'où : dans un arbre, toute arête est un pont. Les ponts sont les points fragiles d'un réseau (une route, un câble dont la coupure isole une partie). [[Complément hors du cours|ⓘ]]

## Arbre couvrant (*spanning tree*)

**Définition.** Soit $G = (V, E, \gamma)$. Un [[Sous-graphe|sous-graphe]] $T$ est un **arbre couvrant** de $G$ si et seulement si $T$ est un arbre **et** un sous-graphe couvrant de $G$.

**Remarque du cours.** Un sous-graphe (couvrant) de $G = (V, E, \gamma)$ est un graphe $G' = (V, E')$ avec $E' \subseteq E$ : mêmes sommets, une partie des arêtes.

Note de l'étudiante : un arbre couvrant de $G$ reprend **tous les nœuds** de $G$ et un sous-ensemble des arêtes tel que le sous-graphe soit un arbre.

**Proposition 6.** Tout graphe **fini connexe** possède au moins un arbre couvrant.

*Preuve du cours* : soit $G$ fini ; tant qu'il reste des arêtes qui ne sont pas des ponts, on en retire une ; le processus termine parce que $E$ est fini.

La preuve s'arrête à la terminaison ; il reste à voir que le graphe obtenu est un arbre couvrant. Il garde **tous les sommets** (on ne retire que des arêtes) ; il reste **connexe**, car retirer une arête qui n'est pas un pont ne change pas le nombre de composantes ; il est **acyclique**, car à la fin toutes ses arêtes sont des ponts, et une arête d'un cycle n'est jamais un pont. [[Complément hors du cours|ⓘ]]

![[Chp2 - tree - image9.png]]
*Figure (« FIG. 2.15 ») : un graphe complet sur a, b, c, d (a–b 2, a–c 6, a–d 3, b–c 3, b–d 7, c–d 1) et un arbre couvrant de coût minimum 6 (a–b 2, b–c 3, c–d 1).*

## Graphe pondéré et arbre couvrant minimal

**Définition (valeur).** Soient $G = (V, E, \gamma, w)$ un [[Graphe pondéré|graphe pondéré]] non orienté et $T = (V, E', \gamma|_{E'})$ un arbre couvrant de $G$, $E' \subseteq E$. La **valeur** de $T$ est
$$w(T) = \sum_{e \in E'} w(e).$$

**Définition (arbre couvrant minimal).** Soit $G = (V, E, w)$ un graphe **simple, connexe, pondéré**. Un **arbre couvrant minimal** (*minimum spanning tree*) de $G$ est un arbre couvrant dont la valeur est **minimale** parmi tous les arbres couvrants de $G$.

### Exemple : sept villes

| Arête | Poids (km) |
|---|---|
| Lille – Brest | 725 |
| Lille – Paris | 222 |
| Lille – Strasbourg | 522 |
| Brest – Paris | 596 |
| Brest – Bordeaux | 623 |
| Strasbourg – Paris | 490 |
| Strasbourg – Nice | 804 |
| Paris – Bordeaux | 583 |
| Paris – Perpignan | 857 |
| Paris – Nice | 932 |
| Bordeaux – Perpignan | 451 |
| Nice – Perpignan | 476 |

![[Chp2 - tree - image3.png]]
*Figure : le graphe $G$ des sept villes, puis un arbre couvrant minimal : Paris relié à Lille (222), Strasbourg (490), Brest (596) et Bordeaux (583) ; Bordeaux – Perpignan (451) ; Perpignan – Nice (476).*

## Trouver un arbre couvrant minimal

### Solution 1 : recherche exhaustive

1. Lister tous les arbres couvrants ;
2. calculer la valeur de chacun ;
3. en choisir un de valeur minimale.

Complexité **exponentielle** : impraticable, trop coûteuse (voir [[Recherche exhaustive]]).

Ordre de grandeur : d'après la **formule de Cayley**, le graphe complet $K_n$ possède $n^{n-2}$ arbres couvrants, soit 16 pour $n = 4$ (le graphe complet de la figure 2.15), 16 807 pour $n = 7$ et environ $2{,}6 \times 10^{23}$ pour $n = 20$. [[Complément hors du cours|ⓘ]]

### Solution 2 : algorithme glouton de Kruskal

Principe ([[Algorithme glouton]]) :
1. initialiser le graphe couvrant **sans arête** ;
2. soit $e$ l'arête **non testée de plus petit poids** : si $e$ ne forme pas de cycle, l'ajouter au graphe couvrant courant ; recommencer.

**[[Algorithme de Kruskal]]** (pseudo-code du cours) :

- *Préconditions* : $G = (V, E, \gamma, w)$ graphe valué **simple et connexe**.
- *Postconditions* : $G(F)$ est un arbre couvrant minimal de $G$.

```
E^c ← E
F ← ∅
tant que card F < card V − 1 faire
    e est choisi dans argmin{w(e), e ∈ E^c}
    E^c ← E^c \ {e}
    si G(F ∪ {e}) est acyclique alors
        F ← F ∪ {e}
    fin si
fin tant que
```

**Théorème 2.5 (terminaison et complexité).** L'algorithme de Kruskal converge vers un arbre couvrant minimum. Sa complexité est
$$O(\text{card}\,E \cdot \log(\text{card}\,V)).$$

Note de l'étudiante : l'algorithme relie tous les nœuds en minimisant la somme des poids des arêtes. [[Erreurs du cours#^e-2-tree|✎]]

D'où vient la complexité : le tri des $m = \text{card}\,E$ arêtes coûte $O(m \log m)$, et comme $m \le n^2$ (avec $n = \text{card}\,V$), $\log m \le 2 \log n$, d'où $O(m \log n)$. Le test « $G(F \cup \{e\})$ est acyclique » revient à vérifier que les deux extrémités de $e$ sont dans des composantes différentes de $G(F)$ ; avec une structure [[Union-Find]] (celle du [[0 - Graph - Python|TP Python]]), chaque test coûte presque un temps constant, si bien que le tri domine. [[Complément hors du cours|ⓘ]]

Pourquoi un choix glouton donne l'optimum : c'est la **propriété de coupe**. Si l'on sépare les sommets en deux groupes, une arête de poids minimal parmi celles qui relient les deux groupes appartient à un arbre couvrant minimal. Quand Kruskal accepte $e$, il la prend comme la plus légère des arêtes qui relient la composante d'une extrémité au reste du graphe : elle est donc sûre. Si tous les poids sont distincts, l'arbre couvrant minimal est **unique** ; sinon, il peut y en avoir plusieurs de même valeur. [[Complément hors du cours|ⓘ]]

Appliqué à un graphe non connexe, l'algorithme (sans la condition d'arrêt $\text{card}\,F < \text{card}\,V - 1$, qu'on remplace par « tant qu'il reste des arêtes ») renvoie une **forêt couvrante minimale** : un arbre couvrant minimal par composante connexe. [[Complément hors du cours|ⓘ]]

L'autre algorithme classique est l'**[[Algorithme de Prim]]** : partir d'un sommet et faire grandir un seul arbre, en ajoutant à chaque étape l'arête la plus légère qui relie l'arbre à un sommet extérieur. Il est lui aussi glouton, et atteint $O(m \log n)$ avec une file de priorité. Kruskal convient bien aux graphes creux, dont on trie facilement les arêtes, Prim aux graphes denses. [[Complément hors du cours|ⓘ]]

Usages : concevoir le réseau le moins cher qui relie des sites (câbles, canalisations, routes, comme l'exemple des villes) ; en fouille de données, couper les arêtes les plus lourdes d'un arbre couvrant minimal donne les groupes de la [[Classification hiérarchique ascendante|classification ascendante]] à saut minimal. [[Complément hors du cours|ⓘ]]

### Déroulé sur l'exemple des villes

Le cours donne le résultat, pas les étapes. Arêtes triées par poids croissant, arrêt à $\text{card}\,V - 1 = 6$ arêtes : [[Complément hors du cours|ⓘ]]

| Étape | Arête testée | Poids | Décision |
|---|---|---|---|
| 1 | Lille – Paris | 222 | ajoutée |
| 2 | Bordeaux – Perpignan | 451 | ajoutée |
| 3 | Nice – Perpignan | 476 | ajoutée |
| 4 | Strasbourg – Paris | 490 | ajoutée |
| 5 | Lille – Strasbourg | 522 | rejetée (cycle Lille – Paris – Strasbourg) |
| 6 | Paris – Bordeaux | 583 | ajoutée |
| 7 | Brest – Paris | 596 | ajoutée : 6 arêtes, arrêt |

Valeur totale : $222 + 451 + 476 + 490 + 583 + 596 = 2818$ km. On retrouve l'arbre de la figure du cours ; les poids étant tous distincts, c'est l'unique arbre couvrant minimal. [[Complément hors du cours|ⓘ]]