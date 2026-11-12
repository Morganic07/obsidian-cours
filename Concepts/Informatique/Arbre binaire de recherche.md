---
type: concept
tags: [year2, year4]
aliases: [arbre binaire de recherche, arbres binaires de recherche, ABR, binary search tree, BST, successeur dans un ABR, get_successor]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf|Chapitre5-ABR.pdf]]", "[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]"]
maj: 2026-11-12
---

Un arbre binaire de recherche (ABR) est un [[Arbre binaire]] dont les clés sont ordonnées : pour chaque nœud, les clés du sous-arbre gauche sont inférieures à la sienne et celles du sous-arbre droit supérieures. Tout sous-arbre d'un ABR est lui-même un ABR (`fils-gauche < parent < fils-droit`). Doublons : la première diapositive du chapitre 5 admet l'égalité (clés « inférieure (ou égale) » à gauche, « supérieure (ou égale) » à droite), les suivantes écrivent des inégalités strictes, et le code `insert` ignore une valeur égale. Cours d'[[Cours/Informatique/Algo/_index|Algo]].

## Propriété clé

Le parcours infixe d'un ABR visite les clés dans l'ordre croissant. Exemple du cours : racine 14, fils 10 et 16, puis 8, 11, 15, 18, parcourus dans l'ordre 8, 10, 11, 14, 15, 16, 18.

## Opérations (code Python du cours)

- **Nœud** (classe `Node`) : `data`, `left`, `right`, `parent`.
- **Insertion** : on compare à la racine puis on descend à gauche si la valeur est plus petite, à droite sinon. Le dernier nœud inspecté devient le parent. Le code du cours ignore une valeur déjà présente.
- **Recherche** : même descente, on s'arrête sur l'égalité ou sur un sous-arbre vide.
- **Minimum** : descendre le plus à gauche possible. **Maximum** : le plus à droite possible.
- **Suppression**, trois cas : feuille (on la retire), un seul enfant (le fils prend sa place), deux enfants (le nœud est remplacé par son successeur, le plus petit nœud du sous-arbre droit, puis le successeur est retiré).

## Limite

Le coût d'une opération dépend de la hauteur de l'arbre (complément : un ABR dégénéré en liste donne une recherche linéaire). L'[[Arbre AVL]] garde la hauteur en $\log_2 n$ par des rotations. Voir aussi la [[Recherche dichotomique]], qui repose sur la même idée de comparaison à la valeur médiane.

## Précisions (complément, hors du cours)

- **Complexité** : recherche, insertion, suppression, minimum et maximum coûtent $O(h)$, où $h$ est la [[Hauteur d'un arbre|hauteur]], avec $\lfloor \log_2 n \rfloor \le h \le n - 1$ pour $n$ nœuds. Si les valeurs arrivent dans un ordre aléatoire, la hauteur moyenne est en $O(\log n)$ ; si elles arrivent triées, chaque insertion ajoute une feuille au bout de la même branche (l'insertion ajoute toujours une feuille) et l'arbre dégénère en liste : $h = n - 1$, opérations en $O(n)$.
- **Caractérisation** : un arbre binaire est un ABR si et seulement si son parcours infixe est croissant. Vérifier seulement chaque père contre ses deux fils ne suffit pas : l'arbre de racine 10, de fils gauche 5 (lui-même de fils 2 et 12) et de fils droit 15 respecte la règle localement, mais 12 est dans le sous-arbre gauche de 10 ; son parcours infixe 2, 5, 12, 10, 15 n'est pas croissant.
- **Tri par ABR** : insérer les $n$ valeurs puis faire un parcours infixe donne la liste triée, en $O(n \log n)$ en moyenne et $O(n^2)$ dans le pire cas (entrée déjà triée).
- **Suppression à deux enfants** : le successeur (minimum du sous-arbre droit) n'a pas de fils gauche, sinon ce fils serait plus petit ; on le retire donc par l'un des deux cas simples. On peut symétriquement utiliser le prédécesseur (maximum du sous-arbre gauche), qui n'a pas de fils droit.

## Graph theory (Year 4)

Le diaporama de révision [[2 - tree revisions années précédentes]] reprend l'ABR à éléments uniques (valeurs du sous-arbre gauche $<$ racine $<$ valeurs du sous-arbre droit, tout sous-arbre est un ABR), avec l'exemple 8 ; 3, 10 ; 1, 6, 14 ; 4, 7, 13. Recherche récursive en $O(\log n)$ si l'arbre est [[Arbre équilibré|équilibré]], $O(n)$ s'il est [[Arbre dégénéré|dégénéré]] ; insertion en feuille (ajouts de 2 et 9) ; suppression d'une feuille (13), d'un nœud à un fils (1) et d'un nœud à deux fils (la racine 8, remplacée par son successeur 9).

Notion parente : [[Arbre binaire]]. Voir aussi : [[Arbre AVL]], [[Arbre rouge-noir]], [[B-arbre]], [[Parcours infixe]].

Résumés : [[5 - ABR]], [[3 - Arbres]], [[6 - AVL]], [[2 - tree revisions années précédentes]]
