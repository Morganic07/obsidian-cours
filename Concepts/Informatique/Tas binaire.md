---
type: concept
tags: [year2, year4]
aliases: [tas, tas binaires, heap, binary heap, tas max, tas min, max-heap, min-heap]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]"]
maj: 2026-11-12
---

**Définition (complément, hors du cours)** : un tas binaire (*heap*) est un [[Arbre binaire]] **quasi-parfait** (tous les niveaux remplis sauf le dernier, rempli de gauche à droite) dont chaque nœud a une clé supérieure ou égale à celles de ses fils : c'est un **tas max**. Dans un **tas min**, chaque clé est inférieure ou égale à celles de ses fils. La racine contient donc le maximum (ou le minimum) de toutes les clés. Contrairement à l'[[Arbre binaire de recherche]], il n'y a aucun ordre entre frères ni entre sous-arbres gauche et droit.

## Représentation dans un tableau

Un arbre quasi-parfait de $n$ nœuds, numérotés niveau par niveau de gauche à droite à partir de 1, se range dans un tableau `T[1..n]` sans pointeurs :

$$\text{fils gauche}(i) = 2i, \qquad \text{fils droit}(i) = 2i + 1, \qquad \text{père}(i) = \left\lfloor i/2 \right\rfloor.$$

(Avec un tableau indicé à partir de 0 : fils $2i+1$ et $2i+2$, père $\lfloor (i-1)/2 \rfloor$.) Sa [[Hauteur d'un arbre|hauteur]] vaut $\lfloor \log_2 n \rfloor$.

## Opérations (tas max)

- **Lecture du maximum** : `T[1]`, en $O(1)$.
- **Insertion** : placer la nouvelle clé dans la case $n+1$, puis la faire **remonter** en l'échangeant avec son père tant qu'elle lui est supérieure. Au plus une comparaison par niveau : $O(\log n)$.
- **Extraction du maximum** : retirer `T[1]`, mettre la dernière case à la racine, puis la faire **descendre** en l'échangeant avec le plus grand de ses fils tant qu'elle est plus petite que lui. $O(\log n)$.
- **Construction d'un tas** à partir d'un tableau quelconque : faire descendre les nœuds $\lfloor n/2 \rfloor, \dots, 1$ ; le coût total est $O(n)$, et non $O(n \log n)$, car la plupart des nœuds sont près des feuilles.

## Usages

- **[[File de priorité]]** : structure qui permet d'insérer un élément avec une priorité et d'extraire le plus prioritaire, utilisée par exemple par l'algorithme de Dijkstra et par les ordonnanceurs.
- **Tri par tas** (*heapsort*) : construire un tas max, puis extraire $n$ fois le maximum en le rangeant en fin de tableau. Coût $O(n \log n)$ dans tous les cas, sur place (sans tableau auxiliaire), mais non stable.

## Dans le cours

Le cours ne nomme pas le tas. Il définit l'arbre binaire quasi-parfait et le numérote niveau par niveau dans [[4 - Arbres binaires]], numérotation qui est exactement celle du tableau d'un tas.

Voir aussi : [[Arbre binaire]], [[Vocabulaire des arbres]], [[Hauteur d'un arbre]], [[Pile et file]], [[Tri par sélection]], [[Tri par insertion]], [[Tri fusion]], [[Complexité algorithmique]].

[[2 - tree revisions années précédentes]] ne le nomme pas non plus ; ses compléments le citent pour ranger un arbre binaire dans un tableau et réaliser une file de priorité.

Résumés : [[4 - Arbres binaires]], [[2 - tree revisions années précédentes]]
