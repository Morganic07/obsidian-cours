---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - dijkstra.pdf|chp4 - dijkstra.pdf]]"]
maj: 2026-11-12
complet: true
enrichi: 2026-11-12
---

Résumé de [[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/chp4 - dijkstra.pdf|chp4 - dijkstra.pdf]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Diaporama de 13 diapositives du cours ING1-GI « Algorithmique procédurale II » de CY Tech (2020-2021) : présentation, principe, exemple déroulé étape par étape, puis deux exercices sans correction. Rangé par l'utilisatrice comme supplément du chapitre [[4 - oriented graphs]]. Voir [[Algorithme de Dijkstra]] et, pour les poids négatifs, [[4 - bellman ford]].

## Présentation

- L'[[Algorithme de Dijkstra|algorithme de Dijkstra]] sert à résoudre le problème du [[Plus court chemin|plus court chemin]].
- Il a été conçu en 1956 et publié en 1959 par l'informaticien néerlandais Edsger W. Dijkstra. [[Erreurs du cours#^e-4-dijkstra|✎]]
- Il s'applique sur un [[Graphe orienté|graphe orienté]] ou [[Graphe non orienté|non orienté]], valué positivement (voir [[Graphe pondéré]]).
- Il construit une [[Arborescence (graphe)|arborescence]] entre un sommet d'origine et tous les autres [[Sommet et arête|sommets]] du graphe, de façon à obtenir le plus court chemin entre ce sommet d'origine et les autres.

Dijkstra l'a imaginé en une vingtaine de minutes, à la terrasse d'un café d'Amsterdam, pour une démonstration de l'ordinateur [[ARMAC]] : calculer le plus court trajet entre deux villes sur une carte simplifiée des Pays-Bas. Il l'a publié trois ans plus tard dans la revue [[Numerische Mathematik]] (« A note on two problems in connexion with graphs », vol. 1, 1959, p. 269-271), article qui traite aussi de l'[[Arbre couvrant minimal|arbre couvrant minimal]]. Source : son entretien avec Philip L. Frana, publié dans *Communications of the ACM* en 2010. [[Complément hors du cours|ⓘ]]

« Valué positivement » s'entend au sens large : les poids nuls sont admis, seuls les poids **négatifs** sont exclus. La longueur d'un [[Chemin (graphe)|chemin]] est la somme des poids de ses arêtes, et la distance $\delta(s, v)$ la longueur d'un plus court chemin de $s$ à $v$. [[Complément hors du cours|ⓘ]]

## Principe

- L'[[Algorithme de Dijkstra|algorithme]] prend en entrée un [[Graphe pondéré|graphe pondéré]] positivement et un [[Sommet et arête|sommet]] d'origine.
- Il construit progressivement un [[Sous-graphe|sous-graphe]], de façon à s'assurer que la distance entre le sommet d'origine et les autres sommets soit minimale.
- Pour ce faire, il faut stocker deux [[Information|informations]] pour chaque sommet :
  - la **distance** (le « poids »), qui correspond au poids cumulé des arêtes depuis l'origine ;
  - le **parent** de chaque sommet, afin de connaître le chemin depuis le sommet d'origine.

Déroulé, tel que l'exemple le montre :
1. **[[Initialisation (programmation)|Initialisation]]** : poids 0 pour l'origine, $\infty$ pour les autres sommets, aucun parent.
2. Choisir le **prochain sommet de poids le plus faible pas encore traité** (marqué `*` une fois traité).
3. Pour chacun de ses voisins non traités, si passer par lui donne un poids plus faible, mettre à jour le poids du voisin et en faire son parent.
4. Recommencer à l'étape 2 jusqu'à ce que tous les sommets soient traités ; les arcs (parent, sommet) forment l'[[Arborescence (graphe)|arborescence]].

L'étape 3 est un [[Relâchement d'un arc|relâchement]] : $d(v) \leftarrow \min\big(d(v),\ d(u) + w(u, v)\big)$. L'étape 2 est une [[Recherche du minimum et du maximum|recherche du minimum]] parmi les sommets non traités. Choisir à chaque fois le sommet le plus proche, sans jamais revenir sur ce choix, fait de Dijkstra un [[Algorithme glouton|algorithme glouton]]. [[Complément hors du cours|ⓘ]]

### Pseudo-code

Le cours ne donne pas de pseudo-code ; voici la version classique, avec un tableau des distances `d`, un tableau des parents (voir [[Pseudo-code]], [[Tableau (programmation)]]) et l'[[Ensemble (mathématiques)|ensemble]] $T$ des sommets traités, que la [[Boucle (programmation)|boucle]] `tant que` agrandit d'un sommet à chaque tour. Si le graphe n'est pas [[Graphe connexe|connexe]], les sommets inaccessibles gardent la distance $\infty$ et l'on s'arrête. [[Complément hors du cours|ⓘ]]

```text
algorithme DIJKSTRA(G, s)
in : G = (S, A, w) un graphe pondéré à poids ≥ 0, s un sommet de S
    pour v ∈ S faire
        d[v] := ∞
        parent[v] := NONE
    d[s] := 0
    T := ∅                                  T : sommets traités
    tant que T ≠ S faire
        u := sommet de S \ T de d[u] minimal
        si d[u] = ∞ alors arrêter          les sommets restants sont inaccessibles
        T := T ∪ {u}
        pour chaque voisin v de u avec v ∉ T faire
            si d[u] + w(u, v) < d[v] alors
                d[v] := d[u] + w(u, v)
                parent[v] := u
    renvoyer (d, parent)
fin algo
```

### Pourquoi c'est juste

**[[Invariant de boucle|Invariant]]** de l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] : pour tout [[Sommet et arête|sommet]] traité $u$, $d[u] = \delta(s, u)$. Quand on choisit $u$, supposons par l'absurde (voir [[Raisonnement par l'absurde]]) un chemin $P$ de $s$ à $u$ plus court que $d[u]$. $P$ quitte l'ensemble $T$ des sommets traités par une arête $(x, y)$, avec $x \in T$ et $y \notin T$ ; comme les arêtes de $x$ ont été [[Relâchement d'un arc|relâchées]], $d[y] \le \delta(s, x) + w(x, y)$, qui est au plus la longueur de $P$ puisque la suite de $P$ est de poids **positif ou nul**. Donc $d[y] < d[u]$, ce qui contredit le choix de $u$ comme minimum. Cela prouve la [[Correction d'un algorithme|correction]] de l'algorithme ; sa [[Terminaison d'un algorithme|terminaison]] vient de ce que chaque tour traite un nouveau sommet. [[Complément hors du cours|ⓘ]]

**Contre-exemple avec un poids négatif** ([[Preuve par contre-exemple]]) : arcs $s \to a$ (2), $s \to b$ (3), $b \to a$ (−2). Dijkstra traite $s$, puis $a$ avec $d[a] = 2$, déclaré définitif, puis $b$ ($d[b] = 3$) ; or $s \to b \to a$ vaut $3 - 2 = 1 < 2$. La preuve tombe car la fin du chemin peut faire baisser sa longueur. Avec des poids négatifs, il faut l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] (voir [[4 - bellman ford]]). Ajouter une même constante à tous les poids ne marche pas : cela pénalise les chemins à beaucoup d'arcs. [[Complément hors du cours|ⓘ]]

### Complexité

Avec $n$ [[Sommet et arête|sommets]] et $m$ arêtes, l'algorithme fait $n$ extractions du minimum et au plus $m$ [[Relâchement d'un arc|relâchements]] dans un [[Graphe orienté|graphe orienté]], $2m$ dans un [[Graphe non orienté|graphe non orienté]] (chaque arête est vue depuis ses deux extrémités : la somme des [[Degré d'un sommet|degrés]] vaut $2m$, voir [[Lemme des poignées de main]]) ; sa [[Complexité algorithmique|complexité]] dépend de la structure qui garde les sommets non traités [[Complément hors du cours|ⓘ]] :

| Structure | Complexité | Adaptée à |
|---|---|---|
| [[Tableau (programmation)\|Tableau]] des distances, recherche linéaire du minimum | $O(n^2)$ | graphes denses ($m$ proche de $n^2$), [[Matrice d'adjacence\|matrice d'adjacence]] |
| [[File de priorité\|file de priorité]] en [[Tas binaire\|tas binaire]] | $O((n + m) \log n)$ | graphes peu denses, [[Liste d'adjacence\|listes d'adjacence]] |
| [[Tas de Fibonacci\|tas de Fibonacci]] | $O(m + n \log n)$ | surtout théorique (Fredman et Tarjan, 1984) |

Quand tous les poids sont égaux, un [[Parcours en largeur|parcours en largeur]], qui utilise une simple file (voir [[Pile et file]]), donne les mêmes [[Plus court chemin|plus courts chemins]] en $O(n + m)$. [[Complément hors du cours|ⓘ]]

## Exemple

**Énoncé** : appliquer l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] sur le graphe ci-dessous en considérant le [[Sommet et arête|sommet]] de départ A, pour obtenir l'arbre des [[Plus court chemin|plus courts chemins]] en partant de ce sommet.

![[4 - dijkstra - p4.jpg]]
*Figure : [[Graphe non orienté|graphe non orienté]] pondéré à 6 sommets ; arêtes A–B (15), A–E (6), B–C (27), B–F (27), C–E (8), C–F (5), E–F (23), E–D (14), et une boucle de poids 5 sur E.*

La [[Sommet et arête|boucle]] sur E ne sert jamais : avec un poids positif, faire un tour sur place ne raccourcit aucun chemin. Le graphe n'est donc pas un [[Graphe simple|graphe simple]], ce qui ne gêne pas l'algorithme. [[Complément hors du cours|ⓘ]]

Tables étape par étape (poids, puis parent entre parenthèses ; `*` = sommet traité) :

| Sommet | Étape 1 : initialisation | Étape 2 : A | Étape 3 : E | Étape 4 : C | Étape 5 : B | Étape 6 : F | Étape 7 : D |
|---|---|---|---|---|---|---|---|
| A | 0 | 0 * | 0 * | 0 * | 0 * | 0 * | 0 * |
| B | ∞ | 15 (A) | 15 (A) | 15 (A) | 15 (A) * | 15 (A) * | 15 (A) * |
| C | ∞ | ∞ | 14 (E) | 14 (E) * | 14 (E) * | 14 (E) * | 14 (E) * |
| D | ∞ | ∞ | 20 (E) | 20 (E) | 20 (E) | 20 (E) | 20 (E) * |
| E | ∞ | 6 (A) | 6 (A) * | 6 (A) * | 6 (A) * | 6 (A) * | 6 (A) * |
| F | ∞ | ∞ | 29 (E) | 19 (C) | 19 (C) | 19 (C) * | 19 (C) * |

Valeurs recalculées : les tables du cours sont exactes. Détail des mises à jour [[Complément hors du cours|ⓘ]] :
- **Étape 2, on traite A** (poids 0) : B = 0 + 15 = 15 et E = 0 + 6 = 6, de parent A.
- **Étape 3, on traite E** (6, le plus faible des non traités) : C = 6 + 8 = 14, D = 6 + 14 = 20, F = 6 + 23 = 29, de parent E.
- **Étape 4, on traite C** (14) : F passe à 14 + 5 = 19 < 29, de parent C ; B via C donnerait 14 + 27 = 41 > 15, inchangé.
- **Étape 5, on traite B** (15) : F via B donnerait 15 + 27 = 42 > 19, rien ne change.
- **Étape 6, on traite F** (19) puis **étape 7, D** (20) : plus rien ne change.

**Étape 8 : construction de l'[[Arborescence (graphe)|arborescence]].** On garde les arêtes (parent, sommet) : A → B (15), A → E (6), E → C (8), E → D (14), C → F (5).

![[4 - dijkstra - p12.jpg]]
*Figure : arborescence des plus courts chemins de racine A, et table finale (A 0 ; B 15, parent A ; C 14, parent E ; D 20, parent E ; E 6, parent A ; F 19, parent C).*

C'est l'[[Arbre des plus courts chemins|arbre des plus courts chemins]] de racine A : un [[Arbre (théorie des graphes)|arbre]] à 6 sommets et 5 arêtes, dans lequel le chemin de A à chaque sommet est un plus court chemin du graphe. Par exemple, pour F on remonte F ← C ← E ← A : A → E → C → F, de longueur 6 + 8 + 5 = 19. [[Complément hors du cours|ⓘ]]

Le même calcul est au cœur de l'[[Algorithme de Prim|algorithme de Prim]], qui construit un [[Arbre couvrant minimal|arbre couvrant minimal]] avec la même structure : seule change la clé d'un sommet, le poids de l'arête qui le rattache à l'arbre au lieu de la distance cumulée depuis l'origine. Les deux arbres diffèrent en général. [[Complément hors du cours|ⓘ]]

## Exercices

![[4 - dijkstra - p13.jpg]]
*Figure : les deux [[Graphe non orienté|graphes non orientés]] des exercices ; à gauche, départ D ; à droite, départ B.*

Pour chacun, appliquer l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] depuis le [[Sommet et arête|sommet]] de départ indiqué et construire l'[[Arborescence (graphe)|arborescence]] des [[Plus court chemin|plus courts chemins]]. Les [[Sommet et arête|boucles]] sont sans effet (poids positifs).

### Exercice 1 : sommet de départ D

Arêtes : A–B (21), B–D (27, tracée en rouge sur la diapositive, sans explication), B–F (13), C–D (25), C–E (6), C–F (7), D–F (1), E–F (9), et une boucle de poids 25 sur D.

**Solution** (non donnée par le cours, calculée et vérifiée par programme) [[Complément hors du cours|ⓘ]] :

| Sommet | Init. | Étape 2 : D | Étape 3 : F | Étape 4 : C | Étape 5 : E | Étape 6 : B | Étape 7 : A |
|---|---|---|---|---|---|---|---|
| A | ∞ | ∞ | ∞ | ∞ | ∞ | 35 (B) | 35 (B) * |
| B | ∞ | 27 (D) | 14 (F) | 14 (F) | 14 (F) | 14 (F) * | 14 (F) * |
| C | ∞ | 25 (D) | 8 (F) | 8 (F) * | 8 (F) * | 8 (F) * | 8 (F) * |
| D | 0 | 0 * | 0 * | 0 * | 0 * | 0 * | 0 * |
| E | ∞ | ∞ | 10 (F) | 10 (F) | 10 (F) * | 10 (F) * | 10 (F) * |
| F | ∞ | 1 (D) | 1 (D) * | 1 (D) * | 1 (D) * | 1 (D) * | 1 (D) * |

- On traite D : B = 27, C = 25, F = 1 (la boucle est ignorée).
- On traite F (1) : B = 1 + 13 = 14 < 27, C = 1 + 7 = 8 < 25, E = 1 + 9 = 10 ; tous de parent F.
- On traite C (8) : E via C donnerait 8 + 6 = 14 > 10, inchangé. On traite E (10) : rien.
- On traite B (14) : A = 14 + 21 = 35. On traite A (35).

Arborescence : D → F (1), F → C (7), F → E (9), F → B (13), B → A (21). L'arête directe B–D (27) n'en fait pas partie : passer par F coûte 14.

### Exercice 2 : sommet de départ B

Arêtes : A–B (6), A–D (4), A–E (3), B–D (17), B–F (28), C–E (10), E–F (18), et des boucles de poids 16 sur A et 26 sur E.

**Solution** (non donnée par le cours, calculée et vérifiée par programme) [[Complément hors du cours|ⓘ]] :

| Sommet | Init. | Étape 2 : B | Étape 3 : A | Étape 4 : E | Étape 5 : D | Étape 6 : C | Étape 7 : F |
|---|---|---|---|---|---|---|---|
| A | ∞ | 6 (B) | 6 (B) * | 6 (B) * | 6 (B) * | 6 (B) * | 6 (B) * |
| B | 0 | 0 * | 0 * | 0 * | 0 * | 0 * | 0 * |
| C | ∞ | ∞ | ∞ | 19 (E) | 19 (E) | 19 (E) * | 19 (E) * |
| D | ∞ | 17 (B) | 10 (A) | 10 (A) | 10 (A) * | 10 (A) * | 10 (A) * |
| E | ∞ | ∞ | 9 (A) | 9 (A) * | 9 (A) * | 9 (A) * | 9 (A) * |
| F | ∞ | 28 (B) | 28 (B) | 27 (E) | 27 (E) | 27 (E) | 27 (E) * |

- On traite B : A = 6, D = 17, F = 28.
- On traite A (6) : D = 6 + 4 = 10 < 17, E = 6 + 3 = 9 ; de parent A.
- On traite E (9) : C = 9 + 10 = 19, F = 9 + 18 = 27 < 28 ; de parent E.
- On traite D (10), puis C (19), puis F (27) : plus rien ne change.

Arborescence : B → A (6), A → E (3), A → D (4), E → C (10), E → F (18).

## Pour aller plus loin

- **En réseau** : dans un [[Réseau|réseau]] de routeurs, avec le [[Routage à état de liens|routage à état de liens]] ([[OSPF]], *Open Shortest Path First*, et IS-IS), chaque [[Routeur|routeur]] connaît la carte complète de sa zone et y lance l'[[Algorithme de Dijkstra|algorithme de Dijkstra]] en se prenant pour source ; l'[[Arbre des plus courts chemins|arbre]] obtenu remplit sa [[Routage statique|table de routage]]. C'est le fonctionnement « global » opposé au fonctionnement « local » de l'[[Algorithme de Bellman-Ford|algorithme de Bellman-Ford]] dans [[4 - bellman ford]] (voir aussi [[Routage dynamique]], [[Routage IP]]). [[Complément hors du cours|ⓘ]]
- **[[Algorithme A étoile|Algorithme A*]]** (Hart, Nilsson et Raphael, 1968) : variante de Dijkstra pour aller vers **une** cible ; on choisit le sommet qui minimise $d(v) + h(v)$, où $h$ est une [[Heuristique (algorithmique)|heuristique]] estimant la distance restante (par exemple la [[Distance|distance]] à vol d'oiseau sur une carte). Si $h$ ne surestime jamais la distance réelle, le chemin trouvé est optimal ; avec $h = 0$, on retrouve Dijkstra. Utilisé en [[Jeu vidéo|jeu vidéo]] et en navigation. [[Complément hors du cours|ⓘ]]
- **Tous les couples** : lancer Dijkstra depuis chaque sommet ; l'[[Algorithme de Floyd-Warshall|algorithme de Floyd-Warshall]] ($O(n^3)$) et l'[[Algorithme de Johnson|algorithme de Johnson]] traitent aussi le cas des poids négatifs sans [[Circuit absorbant|circuit absorbant]]. [[Complément hors du cours|ⓘ]]
- **Arrêt anticipé** : si l'on ne cherche que le chemin vers une cible $t$, on peut s'arrêter dès que $t$ est traité. [[Complément hors du cours|ⓘ]]

## Voir aussi

- [[4 - bellman ford]] : plus courts chemins avec poids négatifs, et application au routage.
- [[4 - oriented graphs]] : [[Graphe orienté|graphes orientés]], [[Parcours en largeur|parcours en largeur]].
- Concepts : [[Algorithme de Dijkstra]], [[Plus court chemin]], [[Arbre des plus courts chemins]], [[Relâchement d'un arc]], [[Algorithme glouton]], [[Graphe pondéré]].
