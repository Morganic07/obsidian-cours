---
type: concept
tags: [year2, year4]
aliases: [arbre n-aire, arbre k-aire, arbre d'arité k]
sources: ["[[Raw/Year 2/Algo/Cours/Chapitre3-Arbres.pdf|Chapitre3-Arbres.pdf]]"]
maj: 2026-11-12
---

Nommé dans le chapitre 3 avec une définition d'une ligne : un arbre m-aire est un arbre d'ordre $m$, dont le degré maximum d'un nœud est égal à $m$. L'[[Arbre binaire]] est le cas $m=2$.

En graph theory, [[2 - tree revisions années précédentes]] l'appelle **arbre k-aire** (ou d'arité $k$) : un [[Arbre numéroté|arbre numéroté]] dont les nœuds ont au plus $k$ fils. Il le décrit comme [[Type abstrait de données|type abstrait]] (`creerArbre`, `ajouterFeuille`, `degre`, `recEnfant`…) et en borne la [[Hauteur d'un arbre|hauteur]] : de $\lceil \log_k((k-1)n+1) \rceil - 1$ à $n - 1$ pour $n$ nœuds.

Notion parente : [[Arbre (théorie des graphes)]]. Voir aussi : [[B-arbre]], [[Arbre ordonné]].

Résumés : [[3 - Arbres]], [[2 - tree revisions années précédentes]]
