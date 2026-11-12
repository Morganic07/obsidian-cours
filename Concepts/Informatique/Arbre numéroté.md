---
type: concept
tags: [year4]
aliases: [arbres numérotés, arbre positionnel, positional tree, enfant absent]
sources: ["[[Raw/Year 4/graph theory/Suppléments de cours (tree, algo...)/Chp2 - tree revisions années précédentes.pdf|Chp2 - tree revisions années précédentes.pdf]]"]
maj: 2026-11-12
---

**Définition** (d'après [[2 - tree revisions années précédentes]]) : un arbre numéroté est un arbre dont les enfants de chaque nœud sont étiquetés par des entiers positifs distincts. Il est ordonné (numéroté → ordonné). Le **$i$-ème enfant** d'un nœud est **absent** si aucun de ses enfants n'est étiqueté par $i$. Un [[Arbre m-aire|arbre k-aire]] (d'arité $k$) a des nœuds d'au plus $k$ fils ; un [[Arbre binaire|arbre binaire]] est d'arité 2.

**Précisions (complément, hors du cours)** : la numérotation permet de dire **où** manque un fils, ce qu'un [[Arbre ordonné|arbre ordonné]] ne fait pas ; c'est ce qui distingue, en arbre binaire, un fils gauche d'un fils droit. Dans l'exemple du cours, la racine 1 a pour enfants 2 et 4 : son 3e enfant est absent. On parle aussi d'arbre positionnel (*positional tree*, dans le manuel de Cormen et al.).

## Dans le cours

[[2 - tree revisions années précédentes]] définit l'arbre numéroté, l'enfant absent, l'arbre k-aire et l'arbre binaire dans sa terminologie.

Notion parente : [[Arbre ordonné]]. Voir aussi : [[Vocabulaire des arbres]], [[Arbre m-aire]], [[Arbre binaire]].

Résumés : [[2 - tree revisions années précédentes]]
