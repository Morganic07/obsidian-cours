---
type: source
tags: [year2]
sources: ["[[qui dit quoi AVL]]"]
maj: 2026-11-06
complet: true
---

Résumé de [[qui dit quoi AVL]], dans [[Algo (matière)]]. Scénario parlé d'un exposé étudiant de 20 diapositives sur les [[Arbre AVL|arbres AVL]], avec le partage de la parole entre trois intervenants (noms non repris ici). Le contenu vient donc des étudiants, pas de l'enseignant. En cas d'écart, le cours et ses images font foi. Le projet correspondant est [[Projet-Arbre-AVL-ID2 (résumé)|Projet-Arbre-AVL-ID2]] ; voir aussi [[AVL momo (résumé)|AVL momo]] et [[ARBRE AVL (résumé)|ARBRE AVL]].

## Répartition de l'exposé

| Diapositives | Partie |
|---|---|
| 1, 2 | Introduction et définition |
| 3, 4 | Notions importantes |
| 5 | Rééquilibrage |
| 6, 7 | Rotations |
| 8, 9 | Résumé des rotations |
| 10, 11, 12 | Présentation des fonctions |
| 13 | Explication des fonctions |
| 14, 15, 16 | Complexité (1) |
| 17, 18, 19 | Complexité (2) |
| 20 | Conclusion |

## Diapositives 1 et 2 : définition

- **AVL = [[Arbre binaire de recherche|ABR]] + rééquilibrage.**
- L'équilibrage fait passer d'un arbre déséquilibré à un arbre équilibré (les deux arbres sont montrés sur la diapositive, absente de la note).
- But : optimiser les opérations de recherche, d'ajout et de suppression.

## Diapositive 3 : hauteur

- Hauteur d'un nœud : « compter le nombre de branches qui le sépare de la racine » (voir point à vérifier 1).
- Hauteur d'un arbre : $h + 1$, où $h$ est la hauteur du plus grand sous-arbre.
- Un nœud inexistant a une hauteur de $-1$.

Voir [[Hauteur d'un arbre]] et [[Vocabulaire des arbres]].

## Diapositive 4 : facteur d'équilibrage

- Il dit si un nœud est équilibré ou non.
- Calcul : $\text{fe}(x) = h(\text{sous-arbre droit}) - h(\text{sous-arbre gauche})$.
- Un arbre est équilibré si **tous** ses nœuds le sont, c'est-à-dire si le facteur de chaque nœud appartient à $\{-1, 0, 1\}$.
- On fait les calculs **en partant du bas**.

## Diapositive 5 : rééquilibrage

Calcul des facteurs d'équilibre des nœuds 17, puis 15, puis 12 sur l'exemple de la diapositive (lecture du texte de gauche ; la diapositive n'est pas dans la note).

## Diapositives 6 et 7 : rotations

- Deux types : **rotation droite** et **rotation gauche** ; on peut en enchaîner plusieurs.
- Cas $\text{fe}(y) = -2$ : le sous-arbre gauche est plus grand. Soit $x$ le fils gauche de $y$ :
  - si $\text{fe}(x) = -1$ ou $0$ : déséquilibre à gauche, on fait une **rotation à droite de $x$ autour de $y$** ;
  - si $\text{fe}(x) = 1$ : $x$ a un sous-arbre droit de racine $z$, qui a lui-même deux sous-arbres. On fait d'abord une **rotation à gauche de $z$ autour de $x$** ; on obtient un facteur de $-1$ pour $z$, ce qui ramène au premier cas ; on fait alors une **rotation à droite de $z$ autour de $y$**. L'arbre est équilibré.
- Diapositive 7 : « la même », c'est-à-dire le cas symétrique ($\text{fe} = 2$).

## Diapositives 8 et 9 : résumé des rotations

- Retour à l'arbre de la diapositive 5 : le nœud 12 a un facteur de 2, déséquilibre à droite. Il faut une **rotation gauche du nœud 15 autour de 12**.
- Un schéma résume les rotations (non reproduit dans la note).

## Diapositives 10 à 12 : présentation des fonctions Python

Organigramme de l'algorithme :

1. Créer un arbre AVL « vide » grâce à une fonction.
2. Ajouter ou supprimer un nœud.
3. Calculer les facteurs d'équilibrage.
4. Si la [[Valeur absolue|valeur absolue]] de chaque facteur vaut 0 ou 1, l'arbre est équilibré : c'est un AVL. Sinon, un nœud est déséquilibré et il faut effectuer des rotations.

Le programme est jugé « assez complexe » car plusieurs fonctions sont imbriquées.

## Diapositive 13 : explication du code

### `hauteur(self)`

Exemple avec la chaîne 9 → 8 → 5 (chaque nœud n'a qu'un fils gauche) :

- `hauteur()` sur 9 appelle `hauteur()` sur son sous-arbre gauche (8), qui l'appelle sur 5 ;
- 5, feuille, « retourne 1 car il n'a pas d'enfants » ;
- en remontant : $1 + \max(\text{gauche}, \text{droite})$ donne 1 pour 5, 2 pour 8, 3 pour 9.

Fonction [[Récursivité|récursive]].

### `rotation_droit(self)`

Arbre A (racine), B (fils gauche de A), C (fils gauche de B) :

```python
new_racine = self.gauche        # la nouvelle racine devient B
self.gauche = new_racine.droit  # B n'a pas de sous-arbre droit : A n'aura rien à gauche
new_racine.droit = self         # le nœud à droite de B est A
```

Résultat : B racine, avec C à gauche et A à droite.

### `ajouter(self, valeur)`

Démonstration avec l'outil graphique AVLTkinter. Arbre avec les nombres de 1 à 8 ; on ajoute 9 en suivant le chemin récursif jusqu'à sa place. En bas à droite, 9 rend $\text{eq}(7) = 2$ : déséquilibre à droite, d'où une **rotation gauche entre 7 et 8**.

![[qui dit quoi AVL - image9.png]]
*Figure : arbre de 1 à 8 avant l'ajout : racine 4 (1), 2 (0) avec 1 et 3, 6 (1) avec 5 (0) et 7 (1), et 8 (0) fils droit de 7.*

![[qui dit quoi AVL - image7.png]]
*Figure : après l'ajout de 9 et la rotation, 6 (1) a pour fils 5 (0) et 8 (0), et 8 a pour fils 7 (0) et 9 (0).*

### `supprimer(self, valeur)`

Démonstration avec AVLTkinter sur l'arbre de 1 à 9. On supprime 6, qui a deux fils : l'algorithme le remplace par la plus petite valeur de son sous-arbre droit, $\min\{7, 8, 9\} = 7$, puis supprime l'ancien 7. Consigne : montrer aussi le cas de la suppression d'une feuille et celui d'un nœud à un seul fils.

![[qui dit quoi AVL - image8.png]]
*Figure : arbre de 1 à 9 avant la suppression : racine 4 (1), 2 (0) avec 1 et 3, 6 (1) avec 5 (0) et 8 (0), 8 avec 7 et 9.*

![[qui dit quoi AVL - image10.png]]
*Figure : après la suppression de 6 : le sous-arbre a pour racine 7 (1), avec 5 (0) à gauche et 8 (1) à droite, et 9 (0) fils droit de 8.*

## Diapositives 14 à 16 : complexité de `ajouter`

- `ajouter` appelle `equilibrer` : il faut d'abord la [[Complexité algorithmique|complexité]] de `equilibrer`.
- L'équilibrage fait un nombre fixe d'opérations : chacune porte sur 3 nœuds et leurs sous-arbres, quelle que soit la hauteur de l'arbre. `equilibrer` ne dépend donc ni de la hauteur ni du nombre de nœuds : **$O(1)$** selon l'exposé (voir point à vérifier 2).
- `ajouter` est récursive et dépend de la hauteur : **$O(h)$**. On veut la complexité en fonction de $n$, pas de $h$.

## Diapositives 17 à 19 : hauteur en fonction de $n$

- Tableau du nombre minimal de nœuds pour chaque hauteur $h = 0, 1, 2, 3$, à faire au tableau.
- « Formule générale » à lire sur la diapositive.
- Graphique du nombre de nœuds en fonction de la hauteur, puis raisonnement lu à droite.

Ces diapositives ne sont pas dans la note : ni la formule ni le raisonnement n'y figurent.

## Diapositive 20

Formule de salutation de clôture.

## Points à vérifier dans le cours

Rien n'a été corrigé dans le cours. Les images sont lues par leurs transcriptions, aucune ouverte. La note contient des consignes de jeu (« lire le texte », « faire au tableau »), sans contenu.

1. **Définition de la hauteur d'un nœud (diapo 3)** (complément). **À corriger avant un examen.** « Compter le nombre de branches qui le sépare de la racine » définit la profondeur, pas la hauteur. La hauteur compte les branches jusqu'à la feuille la plus profonde du sous-arbre. La phrase suivante (« $h + 1$ où $h$ est la hauteur du sous-arbre le plus grand ») suppose bien cette seconde définition.
2. **Complexité de `equilibrer`** : $O(1)$ ici, contre $O(\log n)$ dans [[AVL momo (résumé)|AVL momo]]. Le $O(1)$ ne vaut que si la hauteur est stockée dans les nœuds. Le code montré recalcule la hauteur, ce qui donne $O(n)$.
3. **Hauteur d'une feuille** : $-1$ pour un sous-arbre vide en diapo 3, mais la feuille 5 « retourne 1 » en diapo 13 (le code renvoie 0 pour un sous-arbre vide).
4. **Diapo 6** : « on obtient un facteur d'équilibre de $-1$ pour $z$ » après la première rotation. Non vérifié sur l'image.
5. **Facteurs d'équilibre des arbres 4 (1), 6 (1), 7 (1)** : les alertes des transcriptions (légende coupée à gauche, trait de 9 sur son étiquette) sont des soucis de lecture, sans effet sur le contenu.
6. **Diapos 17 à 19** : la formule et le raisonnement de la hauteur ne figurent pas dans la note ; le contenu manque.
7. **Ajout de 9 (diapo 13)** (complément) : dans la figure d'avant, 8 est fils droit de 7, lui-même fils droit de 6. Avec 9 sous 8, le nœud 7 a bien un facteur 2 et la rotation gauche autour de 7 fait remonter 8 ; la figure d'après montre 8 entre 7 et 9, ce qui est cohérent. Les facteurs affichés après rotation n'ont pas été vérifiés sur l'image.
8. **Figure après suppression (image10)** (complément) : 8 y porte le facteur (1) alors qu'il n'a qu'un fils droit 9, ce qui est cohérent ; mais la racine 7 (1) suppose un sous-arbre gauche de hauteur 0 et un droit de hauteur 1, ce qui l'est aussi. Non vérifié sur l'image.
