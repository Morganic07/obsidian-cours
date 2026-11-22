---
type: concept
tags: [year4]
aliases: [graphe des conflits, graphe de conflits, conflict graph]
sources: ["[[Raw/Year 4/graph theory/chp5 - colorier graph.pdf|chp5 - colorier graph.pdf]]"]
maj: 2026-11-19
---

**Définition (complément, hors du cours)** : graphe qui modélise des contraintes d'exclusion : un sommet par objet (examen, cours, variable, émetteur), une arête entre deux objets qui ne peuvent pas recevoir la même ressource (même créneau, même registre, même fréquence). Une [[Coloration de graphe|coloration propre]] y est une affectation de ressources sans conflit, et le [[Nombre chromatique|nombre chromatique]] le nombre minimum de ressources. C'est la modélisation des problèmes d'emploi du temps, qui a motivé l'[[Algorithme de Welsh-Powell|algorithme de Welsh-Powell]], et de l'[[Allocation de registres|allocation de registres]].

## Dans le cours

Le cours ne le nomme pas, mais son exercice 2 (planifier les examens d'ING3) en est un exemple : le graphe d'incompatibilité des six modules a pour nombre chromatique 3, d'où 9 heures d'examens au minimum ([[5 - colorier graph]]).

Résumés : [[5 - colorier graph]]
