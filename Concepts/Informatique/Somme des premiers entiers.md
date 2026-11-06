---
type: concept
tags:
  - year1
aliases:
  - somme des n premiers entiers
  - nombre triangulaire
  - nombres triangulaires
sources:
  - "[[Cours/Year 1/Algo Maths/Cours 1|Cours 1 (Algo Maths)]]"
  - "[[raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1]]"
  - "[[raw/Year 1/Analyse Maths/Exos/TD0-Rappel.pdf|TD0-Rappel]]"
maj: 2026-11-06
---

$S = 1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$.

**Cours 1** en donne une interprétation géométrique : deux copies de la somme forment un rectangle, $2S = n(n+1)$. **AlgoID1** l'écrit en pseudo-code avec une boucle. Le **TD0** la calcule ($\sum k$, et la somme des impairs $= n^2$). L'examen d'informatique de novembre 2022 demande une fonction « nombre triangulaire ».

Notion parente : [[Symboles somme et produit]]. Voir aussi : [[Récurrence]], [[Carré magique]].

## À vérifier

- Cours 1 : l'annotation finit par « S = n(n+1) », la division par 2 manque.
- Le lien entre nombre triangulaire et cette somme est déduit, non établi par le contrôle (scan).

Résumés : [[Cours 1 - Algo Maths (résumé)|Cours 1 (Algo Maths) (résumé)]], [[AlgoID1 (résumé)]], [[TD0-Rappel (résumé)]], [[Contrôles (résumé)]]
