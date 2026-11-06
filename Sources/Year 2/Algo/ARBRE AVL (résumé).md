---
type: source
sources: ["[[raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL]]"]
maj: 2026-11-06
---

Résumé du PDF [[raw/Year 2/Algo/DM/ARBRE AVL.pdf|ARBRE AVL]] (5 pages, document daté de 2014, pseudo-code), dans [[Year 2 - Algo]]. Le texte est en deux colonnes et l'extraction mélange parfois l'ordre : le fond a été recoupé avec le sujet [[Projet-Arbre-AVL-ID2 (résumé)]].

## Idée générale

Fiche de cours sur l'[[Arbre AVL]] : définition, facteur d'équilibrage, rotations, insertion et suppression, avec les algorithmes en pseudo-code.

## Contenu

- **Définition** : arbre binaire éventuellement vide dont, pour chaque nœud, les hauteurs des sous-arbres gauche et droit diffèrent d'au plus 1 ; les sous-arbres sont eux-mêmes AVL. Nom d'après G.M. Adelson-Velsky et E.M. Landis. Propriété : la hauteur est de l'ordre de $\log_2 n$.
- **Facteur d'équilibrage** : $eq(s) = h(D_s) - h(G_s)$, avec ici la convention $h(\text{NIL}) = 0$ et $h(A) = \text{hauteur}(A) + 1$. Dans un AVL il vaut $-1$, $0$ ou $1$ ; une valeur de $2$ ou $-2$ après une opération déclenche des rotations.
- **Rotation droite autour de $y$** : $y$ descend et son fils gauche $x$ remonte, sans casser l'ordre ; la rotation gauche est l'opération inverse. Seuls les facteurs de $x$ et $y$ changent, avec des formules données pour $eq'(X)$ et $eq'(Y)$.
- **Insertion** : comme dans un [[Arbre binaire de recherche]], avec création d'une feuille. On cherche le premier ancêtre $y$ avec $eq(y) = \pm 2$. Pour $eq(y) = -2$ et $x$ son fils gauche : si $eq(x)$ vaut $-1$ ou $0$, rotation droite ; si $eq(x) = 1$, rotation gauche autour de $x$ puis rotation droite autour de $y$. Le cas $+2$ est symétrique.
- **Suppression** : suppression d'une feuille, puis même détection du premier ancêtre déséquilibré. Trois cas selon $eq(x)$ : $-1$ ou $0$, rotation droite ; $1$, double rotation. Plusieurs rotations peuvent s'enchaîner en remontant, car un déséquilibre en provoque un autre.
- **Implémentation** : cellule `celluleAVL` avec `info`, `hauteur`, `gauche`, `droit`, `père` ; primitives `getHauteur` (1 pour une feuille, 0 pour NIL) et `setHauteur` ; fonctions `rotationDroite`, `rotationGauche`, `ajouter`, `supprimer`, `equilibreAprèsInsertion`, `equilibreAprèsSuppression`, `equilibreUnSommet`. L'intérêt du facteur d'équilibrage est qu'il tient sur 2 bits, mais sa gestion est délicate.

## Liens

Même sujet que [[AVL momo (résumé)]] et [[qui dit quoi AVL (résumé)]], et que le sujet [[Projet-Arbre-AVL-ID2 (résumé)]].

## Points à vérifier

1. **Convention de hauteur** : ce document pose $h(\text{NIL}) = 0$ (hauteur d'une feuille = 1), alors que [[Chapitre3-Arbres (résumé)]] donne $-1$ pour l'arbre vide et 0 pour une feuille. Le facteur d'équilibrage est le même dans les deux conventions, mais il ne faut pas les mélanger.
2. **Condition de boucle de `equilibreAprèsInsertion`** : le texte écrit `eq!=2 et eq!=2` ; la seconde condition devrait être `eq!=-2` pour que la boucle s'arrête dans les deux cas de déséquilibre (complément : lecture du pseudo-code).
