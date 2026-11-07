---
type: concept
tags:
  - year1
aliases:
  - somme des n premiers entiers
  - nombre triangulaire
  - nombres triangulaires
sources:
  - "[[0 - Algo Maths|Cours 1 (Algo Maths)]]"
  - "[[Raw/Year 1/Algo Maths/AlgoID1.pdf|AlgoID1.pdf]]"
  - "[[Raw/Year 1/Analyse Maths/Exos/TD0-Rappel.pdf|TD0-Rappel.pdf]]"
maj: 2026-11-07
---

$S = 1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$.

**Cours 1** en donne une interprétation géométrique : deux copies de la somme forment un rectangle, $2S = n(n+1)$. **AlgoID1** l'écrit en pseudo-code avec une boucle. Le **TD0** la calcule ($\sum k$, et la somme des impairs $= n^2$). L'examen d'informatique de novembre 2022 (page 32 de [[Raw/Year 1/Contrôles.pdf|Contrôles.pdf]]) demande une fonction `triangulaire(n : entier) : booléen` : un nombre triangulaire est le nombre de pastilles d'un triangle (1, 3, 6, 10 sur la figure, avec des rangées de 1, 2, 3 puis 4 pastilles), et $n$ est triangulaire si $\sqrt{8n + 1}$ est entier (exemple : $3 \times 8 + 1 = 25$). L'examen ne relie pas lui-même ces nombres à la formule $\frac{n(n+1)}{2}$.

Notion parente : [[Symboles somme et produit]]. Voir aussi : [[Récurrence]], [[Carré magique]].

## Erreurs du cours

- [[Raw/Year 1/Algo Maths/Cours 1.docx|Cours 1 (Algo Maths)]] écrit, dans le texte du dessin, « 2S = n(n+1) ; S = n(n+1) » ; il faut « S = n(n+1)/2 ».

Résumés : [[0 - Algo Maths|Cours 1 (Algo Maths)]], [[0 - diapo prof]]
