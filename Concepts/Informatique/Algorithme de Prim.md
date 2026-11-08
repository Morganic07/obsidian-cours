---
type: concept
tags: [year4]
aliases: [Prim's algorithm, Prim, algorithme de Prim-Jarník]
matieres: [graph theory]
sources: ["[[Raw/Year 4/graph theory/Chp2 - tree.docx|Chp2 - tree]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : [[Algorithme glouton|algorithme glouton]] de calcul d'un [[Arbre couvrant minimal|arbre couvrant minimal]] d'un [[Graphe pondéré|graphe pondéré]] non orienté [[Graphe connexe|connexe]] à $n$ sommets et $m$ arêtes (Jarník 1930, redécouvert par Prim en 1957 et Dijkstra en 1959).

**Principe** :

1. Choisir un sommet de départ quelconque ; l'arbre courant $T$ ne contient que lui.
2. À chaque étape, parmi les arêtes qui relient un sommet de $T$ à un sommet hors de $T$, ajouter à $T$ celle de poids minimal (avec son extrémité extérieure).
3. S'arrêter quand $T$ couvre les $n$ sommets, soit après $n - 1$ ajouts d'arêtes.

L'arbre grandit à partir d'un seul sommet et reste connexe à chaque étape ; aucune arête ajoutée ne peut fermer de cycle, puisqu'elle mène toujours à un sommet nouveau.

**Correction** : elle découle de la propriété de coupe. Pour toute partition des sommets en deux groupes, une arête de poids minimal parmi celles qui traversent la coupe appartient à un arbre couvrant minimal ; Prim applique cette propriété à la coupe (sommets de $T$, autres sommets).

**Complexité** :

- $O(n^2)$ avec une [[Matrice d'adjacence|matrice d'adjacence]] et un tableau des distances à l'arbre, bien adaptée aux graphes denses ;
- $O(m \log n)$ avec une [[Liste d'adjacence|liste d'adjacence]] et une file de priorité en tas binaire ;
- $O(m + n \log n)$ avec un tas de Fibonacci.

**Comparaison avec l'[[Algorithme de Kruskal]]** :

| | Prim | Kruskal |
|---|---|---|
| Structure | un seul arbre qui grandit | une forêt dont les arbres fusionnent |
| Choix à chaque étape | arête la plus légère sortant de l'arbre | arête la plus légère du graphe ne fermant pas de cycle |
| Outil | file de priorité | tri des arêtes et [[Union-Find]] |
| Adapté à | graphes denses | graphes creux |

Les deux donnent un arbre de même poids total, et le même arbre quand les poids sont distincts.

## Dans le cours

Le cours ne le nomme pas : le chapitre 2 présente l'arbre couvrant minimal et l'algorithme de Kruskal. Prim apparaît dans les compléments de [[2 - tree]].

Voir aussi : [[Arbre couvrant minimal]], [[Algorithme de Kruskal]], [[Algorithme glouton]], [[Union-Find]], [[Complexité algorithmique]], [[Arbre (théorie des graphes)]].

Résumés : [[2 - tree]]
