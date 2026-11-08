---
type: concept
tags: [year2]
aliases: [coords polaires, passage en polaires, polar coordinates]
sources: ["[[Raw/Year 2/Analyse/Chp9-intégrales multiples.pdf|Chp9-intégrales multiples.pdf]]", "[[3 - Limite et continuité d’applications|Chp 3 - Limite et continuité d’applications]]", "[[4 - Calcul différentiel du premier ordre|Chp 4 - Calcul différentiel du premier ordre]]"]
maj: 2026-11-08
---

On pose $x=r\cos\theta$, $y=r\sin\theta$ (ou $\rho$ à la place de $r$).

**Analyse (intégrales multiples)** : en intégrale double, les coordonnées polaires sont adaptées à un domaine en forme de disque ou de cercle.

**Changement de variables en polaires (complément, hors du cours)** :
- jacobien de $(r,\theta) \mapsto (r\cos\theta, r\sin\theta)$ : $J = \begin{vmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{vmatrix} = r\cos^2\theta + r\sin^2\theta = r$, donc $dx\,dy = r\,dr\,d\theta$ (voir [[Matrice jacobienne]]) ;
- le disque de centre $O$ et de rayon $R$ correspond au pavé $[0,R]\times[0,2\pi]$, la couronne $R_1 \le \sqrt{x^2+y^2} \le R_2$ au pavé $[R_1,R_2]\times[0,2\pi]$ ;
- pour un disque de centre $(a;b)$, on pose $x = a + r\cos\theta$, $y = b + r\sin\theta$ (même jacobien $r$) ;
- l'application n'est pas bijective à l'origine ($r = 0$, $\theta$ quelconque) ni sur le bord $\theta \in \{0, 2\pi\}$ ; ces ensembles sont d'aire nulle et ne changent pas la valeur de l'intégrale ;
- exemple : aire du disque, $\displaystyle\int_0^{2\pi}\!\!\int_0^R r\,dr\,d\theta = 2\pi\cdot\frac{R^2}{2} = \pi R^2$.

Application classique : le calcul de l'[[Intégrale de Gauss]]. En dimension 3, les polaires se prolongent en [[Coordonnées cylindriques]] et [[Coordonnées sphériques]].

**Analyse dans Rn** : elles servent à étudier une limite en $(x_0,y_0)$ quand le dénominateur s'y prête. Si le résultat dépend de $\theta$, il n'y a pas de limite ; s'il n'en dépend pas, il faut encore majorer $|\tilde f(\rho,\theta) - \ell| \le g(\rho)$ avec $g(\rho) \to 0$, indépendamment de $\theta$. Contre-exemple : $f(x,y) = \frac{x^2y}{x^4+y^2}$ tend vers 0 le long de chaque droite, mais vaut $\frac12$ sur la parabole $y = x^2$. [[Erreurs du cours#^e-coordonnees-polaires|✎]] Le chapitre 4 traite le changement de variables en polaires sur trois demi-plans ($x>0$, $x<0$, $y>0$).

Voir aussi : [[Intégrale multiple]], [[Limite et continuité]], [[Difféomorphisme]], [[Coordonnées elliptiques]], [[Coordonnées cylindriques]], [[Coordonnées sphériques]], [[Intégrale de Gauss]].

Résumés : [[2 - intégrales multiples]], [[3 - Limite et continuité d’applications]], [[4 - Calcul différentiel du premier ordre]]
