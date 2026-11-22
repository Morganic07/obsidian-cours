---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]]"]
maj: 2026-11-19
complet: true
enrichi: 2026-11-19
---

Résumé de [[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]], dans [[Cours/Informatique/Graph theory/_index|Graph theory]]. Diaporama de 9 diapositives, en anglais, du chapitre 5 : définitions de la [[Coloration de graphe|coloration]] et du [[Nombre chromatique|nombre chromatique]], algorithme exact et [[Algorithme de Welsh-Powell|algorithme de Welsh-Powell]] avec un exemple, propriétés du nombre chromatique, puis deux exercices sans correction (corrigés ici en complément). Suite de [[1 - Undirected graph]], dont il reprend le vocabulaire : [[Graphe non orienté]], [[Sommet et arête|sommets et arêtes]], [[Degré d'un sommet|degré]], [[Graphe complet|graphe complet]], [[Sous-graphe|sous-graphe]].

## Définitions

### Coloration propre

- **Définition (proper coloring, version informelle)** : une **coloration propre** d'un graphe est une attribution de couleurs aux sommets telle que deux [[Sommet et arête|sommets adjacents]] n'aient jamais la même couleur.
- **Définition (proper coloring, version formelle)** : soit $G = (V, E)$ un [[Graphe non orienté|graphe non orienté]] et $C$ un [[Ensemble (mathématiques)|ensemble]] de couleurs. Une **coloration** de $G$ est une [[Application (mathématiques)|application]] $c : V \to C$. Elle est dite **propre** si et seulement si $\forall (v, v') \in E,\ c(v) \neq c(v')$. [[Erreurs du cours#^e-5-colorier-graph|✎]]

La définition formelle se lit avec un [[Quantificateur|quantificateur]] universel et une [[Implication logique|implication]] : pour toute paire de sommets, s'ils sont reliés par une arête, alors leurs couleurs diffèrent. Une coloration quelconque n'a aucune contrainte ; seule la coloration propre en a. Dans la suite, « colorier un graphe » veut toujours dire en donner une coloration propre. [[Complément hors du cours|ⓘ]]

Les sommets d'une même couleur forment un [[Ensemble stable (graphe)|ensemble stable]] (aucune arête entre eux) : une coloration propre en $k$ couleurs revient à une [[Partition d'un ensemble|partition]] de $V$ en $k$ stables, les **classes de couleur**. Un graphe qui a une boucle (arête d'un sommet vers lui-même) n'a aucune coloration propre ; on travaille donc sur des [[Graphe simple|graphes simples]], et les arêtes multiples ne changent rien. [[Complément hors du cours|ⓘ]]

### k-coloration

- **Définition (k-coloring)** : soit $G = (V, E)$ un graphe non orienté et $k$ un entier non nul. Une **$k$-coloration** de $G$ est une coloration $c$ telle que $\text{card}(c(V)) = k$, c'est-à-dire qui utilise exactement $k$ couleurs ($c(V)$ est l'[[Image et image réciproque|image]] de $V$ par $c$, et [[Cardinal d'un ensemble|card]] son nombre d'éléments).
- $G$ est dit **$k$-coloriable** si et seulement s'il existe une $k$-coloration propre de $G$.

Si $G$ est $k$-coloriable et $k < n = \text{card}(V)$, il est aussi $(k+1)$-coloriable : il suffit de repeindre d'une couleur neuve un sommet d'une classe qui en compte au moins deux. Être $k$-coloriable au sens du cours revient donc à « admettre une coloration propre en **au plus** $k$ couleurs », la définition la plus courante dans les manuels. [[Complément hors du cours|ⓘ]]

### Exemple

*Figure : un graphe à 8 sommets et une coloration propre en 4 couleurs (diapositive 2).*

![[5 - colorier graph - p2.jpg]]

Le graphe a 14 arêtes : $FH$, $FE$, $FA$, $HE$, $HA$, $HG$, $EA$, $EB$, $ED$, $AB$, $BG$, $BC$, $GD$, $DC$. La coloration proposée : rouge pour $H$, $B$, $D$ ; vert pour $E$, $G$, $C$ ; bleu pour $A$ ; jaune pour $F$. Aucune arête ne relie deux sommets de même couleur. [[Complément hors du cours|ⓘ]]

### Nombre chromatique et coloration optimale

- **Définition (chromatic number)** : le **[[Nombre chromatique|nombre chromatique]]** d'un graphe $G$ est le nombre minimum de couleurs d'une coloration propre ; on le note $\chi(G)$ :
$$\chi(G) = \min\{\text{card}(c(V)) \mid c \text{ coloration propre de } G\}$$
- **Définition (optimal coloring)** : soit $G = (V, E)$ un graphe non orienté. Une **coloration propre optimale** de $G$ est une $\chi(G)$-coloration propre de $G$.

$\chi$ est la lettre grecque *chi*, initiale de *chroma*, « couleur ». Le minimum existe toujours : en donnant une couleur différente à chaque sommet, on obtient une coloration propre en $n$ couleurs, donc $1 \leq \chi(G) \leq n$. $\chi(G) = 1$ exactement quand $G$ n'a aucune arête. [[Complément hors du cours|ⓘ]]

Trouver $\chi(G)$ est un problème d'[[Optimisation combinatoire|optimisation combinatoire]] : on cherche la meilleure solution parmi un nombre fini, mais énorme, de colorations. [[Complément hors du cours|ⓘ]]

## Recherche d'une coloration

### Algorithme exact

- L'algorithme exact considère chacune des $k^n$ affectations de $k$ couleurs aux $n$ sommets et vérifie pour chacune si elle est propre.
- Il n'est utilisé que pour les plus petits graphes.

Le nombre $k^n$ vient du [[Dénombrement|dénombrement]] des applications d'un ensemble à $n$ éléments vers un ensemble à $k$ éléments : $k$ choix pour chacun des $n$ sommets. Vérifier une affectation coûte $O(m)$, où $m$ est le nombre d'arêtes, d'où une [[Complexité algorithmique|complexité]] en $O(k^n \cdot m)$, exponentielle (voir [[Classe de complexité]]). Pour 3 couleurs et 30 sommets, il y a déjà $3^{30} \approx 2{,}06 \times 10^{14}$ affectations : c'est l'[[Explosion combinatoire|explosion combinatoire]] d'une [[Recherche exhaustive|recherche exhaustive]]. Pour trouver $\chi(G)$, on essaie $k = 1, 2, 3, \ldots$ jusqu'au premier $k$ qui admet une coloration propre. En pratique, les algorithmes exacts explorent les affectations par retour sur trace (*backtracking*) : on colorie les sommets un à un et l'on abandonne une branche dès qu'un conflit apparaît, ce qui évite d'énumérer la plupart des affectations, sans changer le pire cas. [[Complément hors du cours|ⓘ]]

Il est très peu probable qu'on trouve un jour beaucoup mieux : décider si un graphe est 3-coloriable est un problème NP-complet (Garey, Johnson et Stockmeyer, 1976), et calculer le nombre chromatique figure parmi les 21 problèmes NP-complets de Richard Karp (1972) ; voir [[Classes P et NP]]. À l'inverse, décider si un graphe est 2-coloriable est facile : un [[Parcours en largeur|parcours en largeur]] qui colorie alternativement les niveaux y répond en temps linéaire. [[Complément hors du cours|ⓘ]]

### Algorithme de Welsh et Powell

Le cours décrit une classe destinée à implémenter l'[[Algorithme de Welsh-Powell|algorithme de Welsh-Powell]] pour le problème de coloration de graphe. C'est un [[Algorithme glouton|algorithme glouton]] itératif, qui s'exécute sur un graphe statique :

1. Trier tous les sommets par [[Degré d'un sommet|degré]] décroissant dans une liste $V$.
2. Ranger les couleurs dans une liste $C$.
3. Colorier le premier sommet non colorié $v$ de $V$ avec la première couleur disponible de $C$ (disponible : que l'algorithme n'a pas encore utilisée).
4. Parcourir le reste de la liste ordonnée $V$ et donner cette même couleur à chaque sommet non colorié dont aucun voisin n'a déjà cette couleur.
5. Répéter les étapes 3 et 4 jusqu'à ce que tous les sommets soient coloriés.

L'algorithme a été publié par Dominic Welsh et Martin Powell en 1967 (« An upper bound for the chromatic number of a graph and its application to timetabling problems », *The Computer Journal*, 10(1)), justement pour construire des emplois du temps d'examens. Il donne toujours une coloration **propre**, puisqu'un sommet ne reçoit une couleur que si aucun de ses voisins ne l'a déjà, et il **termine** puisque chaque passage colorie au moins un sommet (voir [[Correction d'un algorithme]] et [[Terminaison d'un algorithme]]). [[Complément hors du cours|ⓘ]]

Comme tout algorithme glouton, il ne revient jamais sur un choix, et la coloration obtenue **n'est pas toujours optimale** : c'est une [[Heuristique (algorithmique)|heuristique]], qui donne seulement un [[Majorant et minorant|majorant]] de $\chi(G)$ (l'exercice ci-dessous en donne un exemple). Son résultat dépend aussi de l'ordre choisi entre sommets de même degré. Les auteurs ont démontré que si $d_1 \geq d_2 \geq \ldots \geq d_n$ sont les degrés des sommets $v_1, \ldots, v_n$ dans l'ordre du tri, alors $\chi(G) \leq \max_i \min(d_i + 1,\ i)$. Le tri coûte $O(n \log n)$ (par exemple par [[Tri fusion|tri fusion]]), et chaque passage parcourt au plus toutes les arêtes, soit $O(n \cdot m)$ au pire pour l'ensemble. Une variante plus efficace en pratique est l'[[Algorithme DSATUR|algorithme DSATUR]] (Daniel Brélaz, 1979), qui choisit à chaque étape le sommet dont les voisins portent déjà le plus de couleurs différentes. [[Complément hors du cours|ⓘ]]

Le même principe glouton se retrouve dans l'[[Algorithme de Kruskal|algorithme de Kruskal]] du [[2 - tree|chapitre 2]], mais là il donne toujours l'optimum ; ici non. [[Complément hors du cours|ⓘ]]

### Application de Welsh et Powell

*Figure : le graphe de l'exemple, le tableau des degrés et la coloration obtenue par Welsh et Powell (diapositive 6).*

![[5 - colorier graph - p6.jpg]]

On reprend l'exemple et on trie les sommets par degré décroissant :

| $v$ | E | A | B | H | D | F | G | C |
|---|---|---|---|---|---|---|---|---|
| $d(v)$ | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 2 |

L'algorithme donne la coloration suivante :
- couleur 1 : $E$, $G$ puis $C$ ;
- couleur 2 : $A$ puis $D$ ;
- couleur 3 : $B$ puis $H$ ;
- couleur 4 : $F$.

Le détail du premier passage : $E$ reçoit la couleur 1 ; $A$, $B$, $H$, $D$ et $F$ sont voisins de $E$ et sont sautés ; $G$ ne l'est pas et reçoit la couleur 1 ; $C$ n'est voisin ni de $E$ ni de $G$ et la reçoit aussi. La somme des degrés vaut $5 + 3 \times 4 + 3 \times 3 + 2 = 28 = 2 \times 14$, conformément au [[Lemme des poignées de main|lemme des poignées de main]]. [[Complément hors du cours|ⓘ]]

Ces 4 couleurs sont optimales : $A$, $E$, $F$ et $H$ sont deux à deux adjacents, ils forment une [[Clique (graphe)|clique]] à 4 sommets (un [[Graphe complet|sous-graphe complet]] $K_4$), donc $\chi(G) \geq 4$ d'après la dernière proposition ci-dessous, et $\chi(G) = 4$. [[Complément hors du cours|ⓘ]]

## Propriétés du nombre chromatique

- **Proposition (majorant du nombre chromatique)** : soit $G = (V, E)$ un graphe non orienté et $\Delta = \max\{d(v) \mid v \in V\}$ son degré maximum. Alors $\chi(G) \leq \Delta + 1$.
- **Proposition (nombre chromatique d'un graphe complet)** : soit $n$ un entier non nul. Alors $\chi(K_n) = n$.
- **Proposition (croissance du nombre chromatique)** : soit $G = (V, E)$ un graphe non orienté et $G' = (V', E')$, avec $V' \subseteq V$ et $E' \subseteq E$, un [[Sous-graphe|sous-graphe]] de $G$. Alors $\chi(G') \leq \chi(G)$. [[Erreurs du cours#^e-5-colorier-graph|✎]]
- **Proposition (minorant du nombre chromatique)** : soit $G = (V, E)$ un graphe non orienté. Si $G$ contient un sous-graphe complet à $p$ sommets, alors $\chi(G) \geq p$.

Le cours ne donne pas les démonstrations ; elles sont courtes. [[Complément hors du cours|ⓘ]]

- **Majorant** : on colorie les sommets un par un, dans n'importe quel ordre, avec $\Delta + 1$ couleurs. Quand on arrive à un sommet, ses voisins déjà coloriés sont au plus $\Delta$, ils bloquent au plus $\Delta$ couleurs : il en reste au moins une libre. C'est la coloration gloutonne, dont Welsh-Powell est un cas particulier. [[Complément hors du cours|ⓘ]]
- **Graphe complet** : dans $K_n$, tous les sommets sont deux à deux adjacents, donc ils ont tous des couleurs différentes : il en faut $n$, et $n$ suffisent. [[Complément hors du cours|ⓘ]]
- **Croissance** : la [[Restriction d'une fonction|restriction]] à $V'$ d'une coloration propre de $G$ est une coloration propre de $G'$, puisque toute arête de $G'$ est une arête de $G$ ; elle utilise au plus autant de couleurs. [[Complément hors du cours|ⓘ]]
- **Minorant** : c'est la croissance appliquée au sous-graphe complet $K_p$, dont le nombre chromatique est $p$. Le plus grand $p$ possible s'appelle le **nombre de clique** $\omega(G)$, et l'on a toujours $\omega(G) \leq \chi(G) \leq \Delta + 1$. [[Complément hors du cours|ⓘ]]

Ces deux bornes peuvent être loin de $\chi(G)$. [[Complément hors du cours|ⓘ]]

- Le majorant $\Delta + 1$ est atteint par les graphes complets et par les [[Cycle (graphe)|cycles]] de longueur impaire ($\Delta = 2$, $\chi = 3$), et seulement par eux : d'après le [[Théorème de Brooks|théorème de Brooks]] (1941), un [[Graphe connexe|graphe connexe]] qui n'est ni complet ni un cycle impair vérifie $\chi(G) \leq \Delta$. Une étoile à $n$ branches a $\Delta = n$ mais $\chi = 2$. [[Complément hors du cours|ⓘ]]
- Le minorant $\omega(G)$ peut être très faible : un cycle impair n'a pas de triangle ($\omega = 2$) mais $\chi = 3$, et il existe des graphes sans triangle de nombre chromatique aussi grand qu'on veut (construction de Mycielski, 1955). [[Complément hors du cours|ⓘ]]
- $\chi(G) \leq 2$ si et seulement si $G$ est [[Graphe biparti|biparti]], c'est-à-dire si et seulement s'il n'a aucun cycle de longueur impaire (théorème de Kőnig, 1936). Les [[Arbre (théorie des graphes)|arbres]] à au moins deux sommets sont donc 2-coloriables. [[Complément hors du cours|ⓘ]]
- Pour les [[Graphe planaire|graphes planaires]], le [[Théorème des quatre couleurs|théorème des quatre couleurs]] affirme $\chi(G) \leq 4$ : c'est la forme moderne de la question posée par Francis Guthrie en 1852 sur le coloriage des cartes géographiques (deux pays voisins de couleurs différentes). Kenneth Appel et Wolfgang Haken l'ont démontré en 1976, première grande démonstration à reposer sur un ordinateur ([[Preuve assistée par ordinateur|preuve assistée par ordinateur]]). [[Complément hors du cours|ⓘ]]

## Exercices

### Exercice 1

*Figure : le graphe de l'exercice 1 (diapositive 8).*

![[5 - colorier graph - p8.jpg]]

1. Donner une coloration du graphe en appliquant l'algorithme de Welsh et Powell.
2. Donner une 3-coloration du graphe.
3. Montrer que $\chi(G) = 3$.
4. Conclure.

Correction (le cours n'en donne pas). [[Complément hors du cours|ⓘ]]

Le graphe a 13 arêtes : $AB$, $AC$, $BC$, $BD$, $BF$, $CD$, $CG$, $DE$, $EF$, $EG$, $FG$, $FH$, $GH$. [[Complément hors du cours|ⓘ]]

1. Degrés : $B$, $C$, $F$, $G$ ont degré 4 ; $D$, $E$ degré 3 ; $A$, $H$ degré 2. En départageant par ordre alphabétique, la liste est $B, C, F, G, D, E, A, H$. Couleur 1 : $B$, puis $G$ ($C$, $F$, $D$, $A$ sont voisins de $B$, et $E$, $H$ voisins de $G$). Couleur 2 : $C$, puis $F$. Couleur 3 : $D$, puis $A$ et $H$. Couleur 4 : $E$, voisin de $D$ (couleur 3), de $F$ (couleur 2) et de $G$ (couleur 1). Welsh et Powell donne donc une coloration propre en **4 couleurs**. [[Complément hors du cours|ⓘ]]
2. Une 3-coloration propre : couleur 1 pour $A$, $D$, $G$ ; couleur 2 pour $B$, $E$, $H$ ; couleur 3 pour $C$, $F$. On vérifie les 13 arêtes une à une : aucune ne relie deux sommets de même couleur. [[Complément hors du cours|ⓘ]]
3. $A$, $B$, $C$ forment un triangle, sous-graphe complet $K_3$, donc $\chi(G) \geq 3$ ; la question 2 donne $\chi(G) \leq 3$. Donc $\chi(G) = 3$. [[Complément hors du cours|ⓘ]]
4. L'algorithme de Welsh et Powell n'est pas optimal : il a utilisé 4 couleurs alors que 3 suffisent. Il fournit une coloration propre rapidement, et donc un majorant de $\chi(G)$, mais pas forcément le nombre chromatique : pour le prouver, il faut un minorant égal, ici le triangle. [[Complément hors du cours|ⓘ]]

### Exercice 2 : planifier des examens

On veut planifier les examens de fin de semestre en ING3. Comme des matières sont communes à plusieurs options, on veut mutualiser les épreuves.

- Option 1 : modules $m_1$, $m_2$ et $m_3$.
- Option 2 : modules $m_4$ et $m_6$.
- Option 3 : modules $m_4$ et $m_5$.
- Option 4 : modules $m_3$ et $m_5$.

Sachant que chaque examen dure trois heures, quel est le nombre minimum d'heures nécessaire pour faire passer tous les examens ?

Correction (le cours n'en donne pas). [[Complément hors du cours|ⓘ]]

- On modélise par un [[Graphe d'incompatibilité|graphe d'incompatibilité]] : un sommet par module, et une arête entre deux modules qui ne peuvent pas avoir lieu en même temps parce qu'une même option les contient (ses étudiants passent les deux). Arêtes : $m_1m_2$, $m_1m_3$, $m_2m_3$ (option 1), $m_4m_6$ (option 2), $m_4m_5$ (option 3), $m_3m_5$ (option 4). [[Complément hors du cours|ⓘ]]
- Une couleur est un créneau de trois heures ; une coloration propre est un planning sans conflit, et le nombre minimum de créneaux est $\chi(G)$. [[Complément hors du cours|ⓘ]]
- $m_1$, $m_2$, $m_3$ forment un triangle, donc $\chi(G) \geq 3$. Une 3-coloration : créneau 1 pour $m_1$ et $m_4$, créneau 2 pour $m_2$, $m_5$ et $m_6$, créneau 3 pour $m_3$. Donc $\chi(G) = 3$. [[Complément hors du cours|ⓘ]]
- Il faut **3 créneaux, soit 9 heures** au minimum. [[Complément hors du cours|ⓘ]]

## Applications de la coloration

La coloration modélise tout problème où des objets en conflit doivent recevoir des ressources différentes ; le nombre chromatique est alors le nombre minimum de ressources. [[Complément hors du cours|ⓘ]]

- **Emplois du temps** : examens, cours, réunions, comme dans l'exercice 2 ; c'est l'application qui a motivé Welsh et Powell. [[Complément hors du cours|ⓘ]]
- **[[Allocation de registres]]** : un [[Compilateur|compilateur]] doit ranger les [[Variable (programmation)|variables]] d'un programme dans les quelques [[Registre du processeur|registres du processeur]] ; deux variables vivantes en même temps ne peuvent pas partager un registre. Gregory Chaitin a formulé ce problème comme une coloration de graphe en 1981 ; si le graphe n'est pas coloriable avec le nombre de registres disponibles, des variables sont reléguées en mémoire. [[Complément hors du cours|ⓘ]]
- **Fréquences radio** : deux émetteurs proches doivent utiliser des fréquences différentes pour ne pas se brouiller. [[Complément hors du cours|ⓘ]]
- **[[Sudoku]]** : une grille est une coloration en 9 couleurs (les chiffres) d'un graphe à 81 sommets (les cases), où chaque case est reliée à celles de sa ligne, de sa colonne et de son carré ; résoudre la grille, c'est compléter une coloration partielle. [[Complément hors du cours|ⓘ]]
- **Cartes géographiques** : colorier des pays voisins de couleurs différentes, problème à l'origine du théorème des quatre couleurs. [[Complément hors du cours|ⓘ]]

Pour programmer ces algorithmes, on représente le graphe par une [[Liste d'adjacence|liste d'adjacence]] (dans le TP [[0 - Graph - Python]], un [[Dictionnaire (Python)|dictionnaire]] [[Langage Python|Python]]), plus économe qu'une [[Matrice d'adjacence|matrice d'adjacence]] pour tester les voisins d'un sommet. [[Complément hors du cours|ⓘ]]
