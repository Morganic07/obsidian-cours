---
type: source
tags: [year2]
sources: ["[[qui dit quoi AVL]]"]
maj: 2026-11-05
---

Résumé de [[qui dit quoi AVL]], dans [[Algo (matière)]]. Scénario parlé d'un exposé de 20 diapositives sur les [[Arbre AVL|arbres AVL]], avec le partage de la parole entre trois intervenants (noms non repris ici). En cas d'écart, le cours et ses images font foi.

## Contenu, dans l'ordre de l'exposé

- **Diapositives 1 et 2** : AVL = arbre binaire de recherche + rééquilibrage, pour accélérer recherche, ajout et suppression.
- **3 et 4** : la hauteur d'un nœud vaut $-1$ s'il n'existe pas. Le facteur d'équilibrage est la hauteur du sous-arbre droit moins celle du gauche, il doit être dans $\{-1, 0, 1\}$ en chaque nœud. On calcule en partant du bas.
- **5, 8 et 9** : exemple avec les nœuds 17, 15 et 12. Le nœud 12 a un facteur de 2, déséquilibre à droite, d'où une rotation gauche du nœud 15 autour de 12. Un schéma résume les rotations.
- **6 et 7** : deux types de rotation, droite et gauche, qu'on peut enchaîner. Facteur $-2$ : sous-arbre gauche trop grand. Si le fils gauche a un facteur de $-1$ ou $0$, rotation droite. S'il vaut 1, rotation gauche puis rotation droite.
- **10 à 12** : organigramme du programme : créer un arbre vide, ajouter ou supprimer un nœud, calculer les facteurs, tourner si un facteur sort de $\{-1, 0, 1\}$.
- **13** : explication du code. `hauteur` (exemple avec 9, 8, 5, la feuille 5 renvoie 1), `rotation_droit` (exemple à trois nœuds A, B, C), `ajouter` (ajout de 9 à un arbre de 1 à 8, qui déséquilibre le nœud 7 : rotation gauche entre 7 et 8), `supprimer` (suppression de 6, remplacé par le plus petit de son sous-arbre droit, 7, puis suppression de l'ancien 7).
- **14 à 16** : pour la complexité de `ajouter`, on étudie d'abord `equilibrer`. Le cours dit que `equilibrer` est en $O(1)$ : un nombre fixe d'opérations sur trois nœuds, quelle que soit la hauteur. `ajouter` est récursive et dépend de la hauteur : $O(h)$, qu'il faut exprimer en $n$.
- **17 à 19** : tableau du nombre minimal de nœuds pour chaque hauteur ($h = 0$ à $3$), formule générale, graphique du nombre de nœuds en fonction de la hauteur, raisonnement lu à droite. Ces diapositives ne sont pas détaillées dans la note.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les images sont lues par leurs transcriptions, aucune ouverte. La note contient des consignes de jeu (« lire le texte », « faire au tableau »), sans contenu.

1. **Définition de la hauteur d'un nœud (diapo 3)** (complément). **À corriger avant un examen.** « Compter le nombre de branches qui le sépare de la racine » définit la profondeur, pas la hauteur. La hauteur compte les branches jusqu'à la feuille la plus profonde du sous-arbre. La phrase suivante (« $h + 1$ où $h$ est la hauteur du sous-arbre le plus grand ») suppose bien cette seconde définition.
2. **Complexité de `equilibrer`** : $O(1)$ ici, contre $O(\log n)$ dans [[AVL momo (résumé)|AVL momo]]. Le $O(1)$ ne vaut que si la hauteur est stockée dans les nœuds. Le code montré recalcule la hauteur, ce qui donne $O(n)$.
3. **Hauteur d'une feuille** : $-1$ pour un sous-arbre vide en diapo 3, mais la feuille 5 « retourne 1 » en diapo 13 (le code renvoie 0 pour un sous-arbre vide).
4. **Diapo 6** : « on obtient un facteur d'équilibre de $-1$ pour $z$ » après la première rotation. Non vérifié sur l'image.
5. **Facteurs d'équilibre des arbres 4 (1), 6 (1), 7 (1)** : les alertes des transcriptions (légende coupée à gauche, trait de 9 sur son étiquette) sont des soucis de lecture, sans effet sur le contenu.
6. **Diapos 17 à 19** : la formule et le raisonnement de la hauteur ne figurent pas dans la note ; le contenu manque.
