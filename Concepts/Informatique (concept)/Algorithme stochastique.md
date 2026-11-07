---
type: concept
tags: [year1]
aliases: [algorithmes stochastiques]
sources: ["[[explications DM d'algo (résumé)|explications DM d'algo]]"]
maj: 2026-11-06
---

Algorithme qui intègre du hasard ou des probabilités dans ses décisions, par opposition aux algorithmes déterministes.

Dans le DM du sac à dos, `remplissage_aleatoire` prend chaque objet avec la probabilité $1 - \frac{\text{poids}_{\text{courant}} + w}{P}$, s'il ne fait pas déborder le sac. Il explore d'autres configurations qu'un glouton, mais le résultat varie d'une exécution à l'autre et n'est pas garanti optimal.

Notion parente : [[Problème du sac à dos]]. Voir aussi : [[Algorithme glouton]].

## À vérifier

- La probabilité peut être négative pour un objet trop lourd (il est alors exclu).

Résumés : [[explications DM d'algo (résumé)]]
