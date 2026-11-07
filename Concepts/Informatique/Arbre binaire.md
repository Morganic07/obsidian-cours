---
type: concept
tags: [year2]
aliases: [arbre binaire, arbres binaires, binary tree, parcours préfixe, parcours infixe, parcours postfixe, parcours en profondeur d'un arbre, arbre parfait, arbre quasi-parfait, arbre binaire étiqueté, arbre binaire complet, squelette d'un arbre binaire, fils gauche, fils droit, sous-arbre gauche, sous-arbre droit]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre4-Preing2ID.pdf|Chapitre4-Preing2ID.pdf]]", "[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]"]
maj: 2026-11-06
---

Un arbre binaire est une structure de données hiérarchique où chaque nœud a au plus deux fils. Cours d'[[Cours/Informatique/Algo/_index|Algo]].

## Définition récursive

Un arbre binaire étiqueté est soit l'arbre vide, soit un nœud (la racine, qui porte une étiquette) avec deux arbres binaires : le sous-arbre gauche et le sous-arbre droit. Un arbre non vide est donc un triplet $(v, l, r)$. L'arbre vide n'est pas un nœud. Cette définition rend naturelle la [[Récursivité]] sur les arbres. Le **squelette** d'un arbre binaire est l'arbre sans ses étiquettes.

## Vocabulaire

- **Arité** d'un nœud : son nombre de fils. Une **feuille** a une arité 0.
- **Branche** : chemin de la racine à une feuille ; sa longueur est son nombre d'arêtes.
- **Profondeur** (ou niveau) d'un nœud : nombre d'arêtes qui le séparent de la racine (0 pour la racine).
- **Hauteur** d'un arbre : longueur maximale d'une branche. Le cours donne 0 pour un arbre à un seul nœud et $-1$ pour l'arbre vide.
- **Taille** : nombre de nœuds.

## Arbres particuliers

- **Complet** : aucun nœud d'arité 1.
- **Parfait** : complet, et toutes les feuilles ont le même niveau.
- **Quasi-parfait** : complet jusqu'au niveau $h-1$, feuilles à la profondeur $h$ ou $h-1$, celles de profondeur $h$ le plus à gauche possible. Tout arbre parfait est quasi-parfait.

## Propriétés (par récurrence, voir [[Récurrence]])

Avec $h$ la hauteur, $n$ la taille, $i$ le nombre de nœuds internes et $l$ celui des feuilles :

- $h + 1 \le n \le 2^{h+1} - 1$ ;
- $n = h + 1$ si et seulement si tous les nœuds internes sont d'arité 1 ;
- l'arbre est parfait si et seulement si $n = 2^{h+1} - 1$ ;
- pour un arbre complet, $i = l - 1$ ;
- tout arbre non vide a au moins une feuille (preuve par récurrence sur la taille).

Voir aussi : [[Hauteur d'un arbre]].

## Parcours en profondeur

Le traitement de tous les nœuds se programme par récursion.

| Parcours | Ordre |
|---|---|
| Préfixe | racine, sous-arbre gauche, sous-arbre droit |
| Infixe | sous-arbre gauche, racine, sous-arbre droit |
| Postfixe | sous-arbre gauche, sous-arbre droit, racine |

Sur l'arbre parfait de hauteur 2 de racine 1 (fils 2 et 5, petits-fils 3, 4, 6, 7) : préfixe 1 2 3 4 5 6 7, infixe 3 2 4 1 6 5 7, postfixe 3 4 2 6 7 5 1.

## Liens

- [[Arbre binaire de recherche]] : arbre binaire dont l'infixe est trié.
- [[Arbre AVL]] : arbre binaire de recherche équilibré.
- Les arbres sont des [[Graphe non orienté|graphes non orientés]] acycliques et connexes.
- Le coût d'un parcours ou d'une hauteur se calcule avec le [[Calcul de complexité et théorème de résolution]].

Notion parente : [[Arbre m-aire]].

Résumés : [[4 - Arbres binaires|Chapitre 4]], [[3 - Arbres|Chapitre 3]], [[5 - ABR]]
