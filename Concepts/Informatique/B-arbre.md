---
type: concept
tags: [year2]
aliases: [B-arbres, arbre B, B-tree]
matieres: [Algo]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]"]
maj: 2026-11-08
---

Nommé dans le chapitre 3 avec sa seule définition : un arbre B d'ordre $n$ est un arbre où la racine a au moins deux fils, chaque nœud autre que la racine a entre $n/2$ et $n$ fils, et toutes les feuilles sont au même niveau.

## Précisions (complément, hors du cours)

- La condition « entre $n/2$ et $n$ fils » ne vaut que pour les **nœuds internes** : les feuilles n'ont pas de fils. De même, la racine n'a au moins deux fils que si elle n'est pas elle-même une feuille (arbre réduit à un nœud).
- Chaque nœud contient **plusieurs clés triées**. Un nœud à $m$ fils porte $m - 1$ clés $k_1 < k_2 < \dots < k_{m-1}$, qui séparent ses sous-arbres : le $i$-ème sous-arbre contient les clés comprises entre $k_{i-1}$ et $k_i$. C'est la généralisation de l'[[Arbre binaire de recherche]] à des nœuds larges ; la recherche descend en choisissant, à chaque nœud, l'intervalle qui contient la clé.
- Comme chaque nœud a beaucoup de fils, la hauteur reste très faible (de l'ordre de $\log_{n/2} N$ pour $N$ clés) et toutes les feuilles sont à la même profondeur : l'arbre est équilibré par construction. L'insertion qui remplit trop un nœud le **scinde** en deux et fait remonter la clé médiane vers le père ; c'est ainsi que l'arbre grandit, par la racine.
- Un nœud correspond typiquement à un bloc du disque : peu de niveaux veut dire peu de lectures sur disque. C'est pourquoi les [[Système de gestion de base de données|SGBD]] et de nombreux [[Système de fichiers|systèmes de fichiers]] rangent leurs index dans des B-arbres ou leurs variantes (B+-arbre, où toutes les données sont dans les feuilles).

Notion parente : [[Arbre m-aire]]. Voir aussi : [[Arbre binaire de recherche]], [[Arbre AVL]], [[Arbre rouge-noir]], [[Hauteur d'un arbre]].

Résumés : [[3 - Arbres]]
