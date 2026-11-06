---
type: source
sources: ["[[raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf|Chapitre5-ABR]]"]
maj: 2026-11-06
---

Résumé du PDF [[raw/Year 2/Algo/Cours/Chapitre5-ABR.pdf|Chapitre5-ABR]] (30 diapositives, « Chapitre 5 : Les arbres binaires de recherche », 2024-2025), dans [[Year 2 - Algo]]. Le code est en Python, en programmation objet.

## Idée générale

Définir l'[[Arbre binaire de recherche]] (ABR) et programmer ses opérations : création, insertion, parcours, recherche, minimum, maximum, suppression.

## Contenu, dans l'ordre du cours

- **Définition** : pour chaque nœud, le sous-arbre gauche a des clés inférieures, le droit des clés supérieures, et tout sous-arbre est un ABR. Notation : `fils-gauche < parent < fils-droit`. Le parcours infixe donne les clés dans l'ordre croissant (exemple 14, 10, 16, 8, 11, 15, 18 : 8, 10, 11, 14, 15, 16, 18). Deux exercices demandent de compléter un arbre.
- **Création** : classe `Node` avec `data`, `left`, `right`, `parent`, et les méthodes spéciales `__init__` et `__str__`.
- **Insertion** : comparer à chaque nœud en partant de la racine, aller à gauche si la valeur est plus petite, à droite sinon. Le dernier nœud inspecté est le parent. Code récursif `insert`.
- **Parcours** : fonction `pprint` qui affiche l'arbre couché, en parcours infixe inversé avec le niveau pour l'indentation.
- **Recherche** : méthode `get`, même descente ; exemples $x = 8$ (présent) et $x = 17$ (absent).
- **Minimum et maximum** : descendre le plus à gauche (minimum) ou le plus à droite (maximum).
- **Suppression**, trois cas : feuille, un seul enfant (remplacé par son fils, avec mise à jour du parent), deux enfants (remplacé par son successeur, `get_successor`). Le code est donné sur plusieurs diapositives.
- **Exercice 1** : dessiner un arbre, donner sa hauteur, l'afficher en préfixe, infixe et postfixe.

## Liens

Précédé de [[Chapitre4-Preing2ID (résumé)]]. Le cours suivant, l'[[Arbre AVL]], rééquilibre l'ABR. Pour l'[[Arbre binaire]] et ses parcours, voir le concept.

## Points à vérifier

1. **Définition avec et sans égalité** : la première diapositive autorise « inférieure (ou égale) » et « supérieure (ou égale) », la deuxième écrit des inégalités strictes, et le code de `insert` ignore les valeurs égales. Les doublons ne sont pas traités de façon cohérente.
