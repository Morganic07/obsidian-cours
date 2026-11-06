---
type: concept
aliases: [arbre binaire de recherche, arbres binaires de recherche, ABR, binary search tree, BST]
matieres: [Algo]
sources: ["[[Sources/Year 2/Algo/Chapitre5-ABR (résumé)|Chapitre 5 (résumé)]]", "[[Sources/Year 2/Algo/Chapitre3-Arbres (résumé)|Chapitre 3 (résumé)]]"]
maj: 2026-11-06
---

Un arbre binaire de recherche (ABR) est un [[Arbre binaire]] dont les clés sont ordonnées : pour chaque nœud, les clés du sous-arbre gauche sont inférieures à la sienne et celles du sous-arbre droit supérieures. Tout sous-arbre d'un ABR est lui-même un ABR. Cours d'[[Year 2 - Algo]].

## Propriété clé

Le parcours infixe d'un ABR visite les clés dans l'ordre croissant. Exemple du cours : racine 14, fils 10 et 16, puis 8, 11, 15, 18, parcourus dans l'ordre 8, 10, 11, 14, 15, 16, 18.

## Opérations (code Python du cours)

- **Nœud** : `data`, `left`, `right`, `parent`.
- **Insertion** : on compare à la racine puis on descend à gauche si la valeur est plus petite, à droite sinon. Le dernier nœud inspecté devient le parent. Le code du cours ignore une valeur déjà présente.
- **Recherche** : même descente, on s'arrête sur l'égalité ou sur un sous-arbre vide.
- **Minimum** : descendre le plus à gauche possible. **Maximum** : le plus à droite possible.
- **Suppression**, trois cas : feuille (on la retire), un seul enfant (le fils prend sa place), deux enfants (le nœud est remplacé par son successeur, le plus petit nœud du sous-arbre droit, puis le successeur est retiré).

## Limite

Le coût d'une opération dépend de la hauteur de l'arbre (complément : un ABR dégénéré en liste donne une recherche linéaire). L'[[Arbre AVL]] garde la hauteur en $\log_2 n$ par des rotations. Voir aussi la [[Recherche dichotomique]], qui repose sur la même idée de comparaison à la valeur médiane.
