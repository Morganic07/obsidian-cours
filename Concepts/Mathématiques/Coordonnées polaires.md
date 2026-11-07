---
type: concept
tags: [year2]
aliases: [coords polaires, passage en polaires, polar coordinates]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]", "[[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]]", "[[4 - Calcul différentiel du premier ordre|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-07
---

On pose $x=r\cos\theta$, $y=r\sin\theta$ (ou $\rho$ à la place de $r$).

**Analyse (intégrales multiples)** : en intégrale double, les coordonnées polaires sont adaptées à un domaine en forme de disque ou de cercle.

**Analyse dans Rn** : elles servent à étudier une limite en $(x_0,y_0)$ quand le dénominateur s'y prête. Le chapitre 4 traite le changement de variables en polaires sur trois demi-plans ($x>0$, $x<0$, $y>0$).

Voir aussi : [[Intégrale multiple]], [[Limite et continuité]], [[Difféomorphisme]], [[Coordonnées elliptiques]].

## Erreurs du cours

- [[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]] écrit : « Si le résultat ne dépend pas de $\theta$ alors la fonction $f$ admet une limite » ; il faut que $\tilde f(\rho, \theta)$ tende vers sa limite uniformément en $\theta$, par exemple $|\tilde f(\rho,\theta) - \ell| \le g(\rho)$ avec $g(\rho) \to 0$. Contre-exemple : $f(x,y) = \frac{x^2y}{x^4+y^2}$ tend vers 0 le long de chaque droite, mais vaut $\frac12$ sur la parabole $y = x^2$ (complément, hors du cours). L'étape 3 du même cours ($|f(x,y) - l_c| \to 0$) reste la bonne vérification.

Résumés : [[2 - intégrales multiples]], [[3 - Limite et continuité d’applications]], [[4 - Calcul différentiel du premier ordre]]
