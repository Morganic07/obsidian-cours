---
type: source
tags: [year2]
sources: ["[[raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID]]"]
maj: 2026-11-06
---

Résumé du PDF [[raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID]] (63 diapositives, « Chapitre 4 : Les arbres binaires », 2024-2025, format beamer avec animations), dans [[Algo (matière)]]. Les exemples sont en Python.

## Idée générale

Définir l'[[Arbre binaire]], son vocabulaire et ses propriétés, puis le parcourir et le coder. Le cours insiste sur le gain de temps d'un arbre par rapport aux listes, piles et files (« 10000 ans → quelques secondes »).

## Contenu, dans l'ordre du cours

- **Définition récursive** : un arbre binaire étiqueté est l'arbre vide, ou un nœud (racine, étiquette) avec un sous-arbre gauche et un sous-arbre droit, soit un triplet $(v, l, r)$. L'arbre vide n'est pas un nœud. Exemple : $(1, (42,(),()), (100,(),(123,(),())))$. Squelette : l'arbre sans étiquettes.
- **Vocabulaire** : sous-arbre enraciné en $x$, fils gauche et droit, père, arité, feuille (arité 0), arête, branche (de la racine à une feuille), hauteur (longueur maximale d'une branche, 4 dans l'exemple), taille (nombre de nœuds, 9), profondeur ou niveau.
- **Arbres particuliers** : complet (aucun nœud d'arité 1), parfait (complet, feuilles au même niveau), quasi-parfait.
- **Propriétés par récurrence** : preuve détaillée que tout arbre non vide a une feuille, par récurrence sur la taille avec $n = 1 + n(l) + n(r)$. Autres propriétés : $h+1 \le n \le 2^{h+1}-1$ ; arbre parfait si et seulement si $n = 2^{h+1}-1$ ; arbre complet : $i = l - 1$. Voir [[Récurrence]].
- **Parcours en profondeur** : préfixe, infixe, postfixe. Sur l'arbre parfait de hauteur 2 : 1 2 3 4 5 6 7, 3 2 4 1 6 5 7 et 3 4 2 6 7 5 1.
- **Implémentation Python** : une classe `ArbreBinaire` (valeur, enfants gauche et droit, insertion à gauche et à droite, accesseurs), puis un exercice avec des dictionnaires `noeud(nom, fg, fd)` pour un arbre de racine `r` à 12 nœuds.
- **Fonctions récursives de l'exercice** : `construit` convertit l'arbre en liste imbriquée (`[]` pour le vide, `['r', ['a', [], []], ...]`) ; `hauteur` renvoie $-1$ pour `[]` et sinon le maximum des hauteurs des fils plus 1 ; trois fonctions de parcours. Résultats annoncés : préfixe r,a,c,h,d,i,j,m,b,e,k,f ; postfixe h,c,i,m,j,d,a,k,e,f,b,r ; infixe c,h,a,i,d,m,j,r,k,e,b,f.

## Liens

Précédé de [[Chapitre3-Arbres (résumé)]], suivi de [[Chapitre5-ABR (résumé)]]. Voir aussi [[Récursivité]] et [[Arbre AVL]].
