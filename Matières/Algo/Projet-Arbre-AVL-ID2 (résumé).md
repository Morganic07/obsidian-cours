---
type: source
tags: [year2]
sources: ["[[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf|Projet-Arbre-AVL-ID2.pdf]]"]
maj: 2026-11-06
complet: true
---

Résumé du PDF Projet-Arbre-AVL-ID2 ([[Raw/Year 2/Algo/DM/Projet-Arbre-AVL-ID2.pdf|Projet-Arbre-AVL-ID2.pdf]]) (2 pages), sujet de projet du module « Algorithmique et programmation 3 », groupe Preing2-ID, 2024-2025, dans [[Algo (matière)]].

## Introduction du sujet

- Le nom AVL vient de ceux qui ont créé cette structure : **Adelson-Velskii et Landis**. L'intérêt d'un arbre AVL se situe dans la **recherche**.
- Les [[Arbre AVL|arbres AVL]] sont des [[Arbre binaire de recherche|arbres de recherche]] **équilibrés** : pour chaque nœud, les hauteurs du sous-arbre gauche et du sous-arbre droit diffèrent au plus de 1.
- L'insertion et la suppression dans un AVL nécessitent d'effectuer **des rotations**.
- Les AVL reposent sur le **facteur d'équilibrage** d'un nœud : la différence entre la hauteur de son sous-arbre droit et celle de son sous-arbre gauche,
$$\text{fe}(x) = h(\text{droit}(x)) - h(\text{gauche}(x)).$$

## Exemples d'arbres AVL

![[Projet-Arbre-AVL-ID2 - p1.jpg]]
*Figure : trois formes d'arbres AVL ; nœuds internes en noir, feuilles vides en blanc.*

![[Projet-Arbre-AVL-ID2 - p2.jpg]]
*Figure 1 du sujet : trois AVL étiquetés avec le facteur de chaque nœud : 7 (−1) avec 5 (0) [4, 6] et 8 ; f (−1) avec c (−1) [a (1) → b, d] et h (1) → i ; g (1) avec d (−1) → a et r (−1) [k (0) → j, q ; s].*

Dans ces exemples, tous les facteurs sont dans $\{-1, 0, 1\}$, avec la convention droite moins gauche.

## Le travail demandé

1. Présenter le principe des arbres AVL.
2. Décrire et présenter **en détail** la notion de facteur d'équilibrage et de rotation d'un arbre AVL : rotation simple gauche, rotation simple droite, rotation double droite-gauche, rotation double gauche-droite, etc., pour l'insertion et la suppression des nœuds.
3. La notion de **rééquilibrage** après insertion et suppression d'un nœud.
4. Les **algorithmes en Python** qui implémentent toutes ces fonctions.
5. Trouver **la complexité** de certaines fonctions, par exemple l'insertion et/ou la suppression d'un nœud dans un arbre AVL.

Le sujet ne donne ni barème, ni date de rendu, ni forme imposée.

## Notions mobilisées

[[Arbre AVL]], [[Arbre binaire de recherche]], [[Hauteur d'un arbre]], [[Calcul de complexité et théorème de résolution]] et [[Récursivité]]. Le sujet est celui des exposés résumés dans [[AVL momo (résumé)]] et [[qui dit quoi AVL (résumé)]] (complément : lien déduit du thème commun). Un cours de référence est résumé dans [[ARBRE AVL (résumé)]].

## Points à vérifier

- **« Trouvez la complexité de quelles fonctions »** : formulation du sujet, sans doute pour « de quelques fonctions ».
- **Première figure** : les trois arbres en noir et blanc ne portent pas d'étiquette ; leur caractère AVL n'a pas été vérifié nœud par nœud.
