---
type: concept
tags: [year1]
aliases: [énumération exhaustive]
sources: ["[[Raw/Year 1/Algo Maths/explications DM d'algo .docx|explications DM d'algo]]"]
maj: 2026-11-07
---

Dans le DM du sac à dos : parcourir les $2^n$ configurations d'objets et garder celle de meilleure valeur parmi celles de poids total $\le P$.

`exhaustif_binaire` recalcule tout pour chaque configuration ; `exhaustif_binaire_optimise` calcule la valeur et le poids par incrément, et fait un `break` dès que le poids dépasse $P$.

Notion parente : [[Problème du sac à dos]]. Voir aussi : [[Numération binaire]], [[Code de Gray]].

Résumés : [[2 - tree (résumé)]]
