---
type: concept
tags: [year2]
aliases: [ensemble compact, partie bornée, compact set, théorème de Heine]
matieres: [Analyse dans Rn]
sources: ["[[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]]", "[[Raw/Year 2/Analyse dans Rn/Chp 2 : éléments de topologie dans Rn.docx|Chp 2 - éléments de topologie dans Rn]]", "[[Raw/Year 2/Analyse dans Rn/Chp 3 : Limite et continuité d’applications.docx|Chp 3 - Limite et continuité d’applications]]"]
maj: 2026-11-08
---

**Définition (complément, hors du cours)** : dans $\mathbb{R}^n$ (et plus généralement dans un espace vectoriel normé), une partie $K$ est compacte si toute suite d'éléments de $K$ admet une [[Suite extraite|suite extraite]] qui converge vers un élément de $K$. En dimension finie, les compacts sont exactement les parties [[Ouvert et fermé|fermées]] et bornées (conséquence du [[Théorème de Bolzano-Weierstrass]]). Une fonction continue à valeurs réelles sur un compact non vide est bornée et atteint ses bornes.

**Partie bornée (complément, hors du cours)** : $A$ est bornée si elle est contenue dans une boule, c'est-à-dire $\exists M > 0, \forall x \in A, \|x\| \le M$. En dimension finie, toutes les normes sont équivalentes, donc cette propriété ne dépend pas de la [[Norme|norme]] choisie.

**Exemples (complément, hors du cours)** :

- compacts de $\mathbb{R}^n$ : un segment $[a, b]$, les boules fermées, les sphères, les pavés $[a_1, b_1] \times \dots \times [a_n, b_n]$ ;
- non compacts : $\mathbb{R}$ (fermé mais non borné), $]0, 1]$ (borné mais non fermé : la suite $1/n$ converge vers $0 \notin\, ]0, 1]$).

**Propriétés des fonctions continues sur un compact (complément, hors du cours)** :

- **bornes atteintes** : si $K \subset \mathbb{R}^n$ est un compact non vide et $f : K \to \mathbb{R}$ est continue, $f$ est bornée et atteint son minimum et son maximum (voir [[Théorème des bornes atteintes]]) ;
- **théorème de Heine** : une fonction continue sur un compact y est uniformément continue (voir [[Continuité uniforme]]).

## Dans le cours

Nommé dans [[2 - éléments de topologie dans Rn|Chp 2 - éléments de topologie dans Rn]] sans définition : le sommaire du chapitre annonce « ouvert, fermé et compact », mais la note ne traite pas les compacts.

À distinguer du [[Compact élémentaire]] du chapitre 9 d'Analyse.

Notion parente : [[Ouvert et fermé]]. Voir aussi : [[Théorème des bornes atteintes]], [[Continuité uniforme]], [[Norme]], [[Extremum local d'une fonction de deux variables]].

Résumés : [[2 - éléments de topologie dans Rn]], [[3 - Limite et continuité d’applications]]
