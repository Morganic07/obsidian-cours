---
type: concept
tags: [year1]
aliases: [algorithmes stochastiques]
sources: ["[[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]]"]
maj: 2026-11-07
---

Algorithme qui intègre du hasard ou des probabilités dans ses décisions, par opposition aux algorithmes déterministes.

Dans le DM du sac à dos, `remplissage_aleatoire` prend chaque objet avec la probabilité $1 - \frac{\text{poids}_{\text{courant}} + w}{P}$, s'il ne fait pas déborder le sac. Il explore d'autres configurations qu'un glouton, mais le résultat varie d'une exécution à l'autre et n'est pas garanti optimal.

Notion parente : [[Problème du sac à dos]]. Voir aussi : [[Algorithme glouton]].

Résumés (rapprochement, complément hors du cours) : [[2 - tree]]
