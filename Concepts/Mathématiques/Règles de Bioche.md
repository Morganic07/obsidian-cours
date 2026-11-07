---
type: concept
tags:
  - year2
aliases:
  - Bioche
  - t = tan(x/2)
matieres:
  - Analyse
sources:
  - "[[1 - Integration|Chap7-Integration]]"
  - "[[0 - Intégration UTILITAIRE|Intégration UTILITAIRE]]"
maj: 2026-11-06
---

Choix d'un changement de variable pour intégrer une fraction en $\sin$ et $\cos$. Avec $\omega(x)=f(x)\,dx$ ([[1 - Integration|Chap7-Integration]]) :

- si $\omega(-x)=\omega(x)$, poser $u=\cos x$ ;
- si $\omega(\pi-x)=\omega(x)$, poser $u=\sin x$ ;
- si $\omega(\pi+x)=\omega(x)$, poser $u=\tan x$.

[[0 - Intégration UTILITAIRE|Intégration UTILITAIRE]] écrit les mêmes règles sur $f$ (par exemple $f(-x)=-f(x)$ donne $t=\cos x$) : les deux formulations sont équivalentes.

Les règles ne fonctionnent pas toujours ; le changement $t=\tan(x/2)$ marche toujours mais demande plus de calculs.

Exemple : $\int \frac{\cos x}{2-\cos^2 x}\,dx=\arctan(\sin x)+c$.

Notion parente : [[Changement de variable dans une intégrale]]. Voir aussi : [[Primitive]].

Résumés : [[1 - Integration]], [[0 - Intégration UTILITAIRE]], [[1 - démonstrations]]
