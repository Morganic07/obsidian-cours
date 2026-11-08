---
type: concept
tags: [year2]
aliases: [coords elliptiques]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]"]
maj: 2026-11-08
---

Changement de variables adapté à un domaine en forme d'[[Ellipse|ellipse]] : $x=ar\cos\theta$, $y=br\sin\theta$, de jacobien $J_\varphi=abr$.

**Compléments (hors du cours)** :
- calcul du jacobien : $J_\varphi = \begin{vmatrix}a\cos\theta & -ar\sin\theta\\ b\sin\theta & br\cos\theta\end{vmatrix} = abr\cos^2\theta + abr\sin^2\theta = abr$, donc $dx\,dy = abr\,dr\,d\theta$ ;
- domaine : en remplaçant dans $\frac{x^2}{a^2}+\frac{y^2}{b^2}\le 1$, on trouve $r^2\cos^2\theta + r^2\sin^2\theta = r^2 \le 1$ ; l'intérieur de l'ellipse correspond donc à $0\le r\le 1$, $0\le\theta\le 2\pi$ ;
- aire de l'ellipse : $\displaystyle\int_0^{2\pi}\!\!\int_0^1 abr\,dr\,d\theta = 2\pi\cdot\frac{ab}{2} = \pi ab$, qui redonne $\pi R^2$ pour $a = b = R$.

Notion parente : [[Coordonnées polaires]]. Voir aussi : [[Intégrale multiple]].

Résumés : [[2 - intégrales multiples]]
