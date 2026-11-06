---
type: concept
tags: [year1]
aliases: [codes de Gray, Gray code]
sources: ["[[explications DM d'algo]]"]
maj: 2026-11-06
---

Suite de codes binaires où deux valeurs successives ne diffèrent que d'un [[Bit]]. Dans le DM du sac à dos, `code_gray(n)` part de `[0]` et, à chaque tour $i$, ajoute les éléments déjà présents parcourus à l'envers avec le bit $i$ mis à 1. `exhaustif_gray` parcourt ces codes.

Notion parente : [[Numération binaire]]. Voir aussi : [[Recherche exhaustive]], [[Problème du sac à dos]].

## À vérifier

- Le code encadré appelle `gray_code` au lieu de `code_gray`, et recalcule chaque configuration : l'intérêt du code de Gray (un seul bit change d'une configuration à la suivante) n'est pas exploité.

Résumés : [[explications DM d'algo (résumé)]]
