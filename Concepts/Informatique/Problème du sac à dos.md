---
type: concept
tags: [year1]
aliases: [sac à dos, knapsack, knapsack problem]
matieres: [Algo Maths]
sources: ["[[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]]"]
maj: 2026-11-07
---

Étant donné $n$ objets de valeur $v$ et de poids $w$, et un sac de capacité $P$, choisir des objets entiers (pris ou non, pas de fraction) de valeur totale maximale sans dépasser $P$. Il y a $2^n$ configurations.

Dans le devoir, un fichier donne sur sa première ligne le nombre d'objets et la capacité $P$, puis la valeur et le poids de chaque objet.

Approches du devoir : [[Recherche exhaustive|énumération exhaustive]] (par nombres binaires, version optimisée, ou par [[Code de Gray]]), [[Algorithme glouton]] (tri par valeur, par poids ou par densité valeur/poids), [[Algorithme stochastique]], [[Programmation dynamique]] (annoncée, non rédigée). Aucun des gloutons n'est optimal dans le cours.

Voir aussi : [[Recherche exhaustive]], [[Code de Gray]], [[Algorithme glouton]], [[Algorithme stochastique]], [[Programmation dynamique]]

## Erreurs du cours

- [[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]] commente `NbObjets, P = map(int, lignes[0].split())` en disant que `split` sert à récupérer « le nombre d'objet et la valeur de chaque objet » ; il faut « le nombre d'objets et la capacité $P$ du sac », ce que le code lit réellement (et ce que dit le début du même commentaire).

Résumés (rapprochement, complément hors du cours) : [[2 - tree]], [[0 - diapo prof]]
